import os
import sys
import time

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from datasets import load_dataset, Dataset
from sklearn.model_selection import GroupShuffleSplit
from tqdm import tqdm


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# PROJECT IMPORTS
# ============================================================

from src.data.dataset import PlantDiseaseDataset

from src.data.preprocessing import (
    get_train_transform,
    get_eval_transform
)

from src.models.cnn import PlantDiseaseCNN


# ============================================================
# CONFIGURATION
# ============================================================

DATASET_NAME = "geraldmc/plantvillage-full"
DATASET_REVISION = "v0.1.0"

NUM_CLASSES = 38

BATCH_SIZE = 32

NUM_EPOCHS = 20
EARLY_STOPPING_PATIENCE = 5

LEARNING_RATE = 1e-3
WEIGHT_DECAY = 1e-4

RANDOM_STATE = 42

NUM_WORKERS = 0

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "baseline_cnn_best.pth"
)

HISTORY_PATH = os.path.join(
    PROJECT_ROOT,
    "results",
    "metrics",
    "baseline_training_history.pt"
)


# ============================================================
# DEVICE
# ============================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# ============================================================
# LOAD PLANTVILLAGE DATASET
# ============================================================

def load_plantvillage():

    print()
    print("=" * 70)
    print("LOADING PLANTVILLAGE DATASET")
    print("=" * 70)

    dataset_dict = load_dataset(
        DATASET_NAME,
        revision=DATASET_REVISION
    )

    # --------------------------------------------------------
    # This dataset is returned as a DatasetDict with a single
    # Hugging Face split called "train".
    #
    # The actual PlantVillage train/test information is stored
    # inside the "split" column.
    # --------------------------------------------------------

    print()
    print(
        f"Hugging Face dataset splits: "
        f"{list(dataset_dict.keys())}"
    )

    # --------------------------------------------------------
    # Get the actual 54,304-row Dataset
    # --------------------------------------------------------

    dataset = dataset_dict["train"]

    print()
    print(
        f"Total samples: "
        f"{len(dataset)}"
    )

    # --------------------------------------------------------
    # Show the values in the dataset's "split" column
    # --------------------------------------------------------

    split_values = dataset.unique("split")

    print()
    print(
        f"PlantVillage split values: "
        f"{split_values}"
    )

    # --------------------------------------------------------
    # Separate official training data
    # --------------------------------------------------------

    train_dataset = dataset.filter(
        lambda example:
        example["split"] == "train"
    )

    # --------------------------------------------------------
    # Separate official test data
    # --------------------------------------------------------

    test_dataset = dataset.filter(
        lambda example:
        example["split"] == "test"
    )

    print()
    print(
        f"Official train samples: "
        f"{len(train_dataset)}"
    )

    print(
        f"Official test samples : "
        f"{len(test_dataset)}"
    )

    return (
        train_dataset,
        test_dataset
    )


# ============================================================
# CREATE GROUP-AWARE TRAIN / VALIDATION SPLIT
# ============================================================

def create_train_validation_split(
    train_dataset
):

    print()
    print("=" * 70)
    print("CREATING GROUP-AWARE TRAIN / VALIDATION SPLIT")
    print("=" * 70)

    # --------------------------------------------------------
    # Convert only the actual Dataset to pandas
    # --------------------------------------------------------

    train_df = train_dataset.to_pandas()

    # --------------------------------------------------------
    # GroupShuffleSplit
    #
    # The same leaf_id will never appear in both train and
    # validation sets.
    # --------------------------------------------------------

    splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=0.10,
        random_state=RANDOM_STATE
    )

    train_indices, val_indices = next(
        splitter.split(
            train_df,
            groups=train_df["leaf_id"]
        )
    )

    # --------------------------------------------------------
    # Training split
    # --------------------------------------------------------

    train_df_split = train_df.iloc[
        train_indices
    ].reset_index(drop=True)

    # --------------------------------------------------------
    # Validation split
    # --------------------------------------------------------

    val_df_split = train_df.iloc[
        val_indices
    ].reset_index(drop=True)

    print()
    print(
        f"Training samples  : "
        f"{len(train_df_split)}"
    )

    print(
        f"Validation samples: "
        f"{len(val_df_split)}"
    )

    # --------------------------------------------------------
    # Convert back to Hugging Face Dataset
    # --------------------------------------------------------

    train_dataset_split = Dataset.from_pandas(
        train_df_split,
        preserve_index=False
    )

    val_dataset_split = Dataset.from_pandas(
        val_df_split,
        preserve_index=False
    )

    # --------------------------------------------------------
    # Restore Hugging Face Image feature
    # --------------------------------------------------------

    from datasets import Image as HFImage

    train_dataset_split = (
        train_dataset_split.cast_column(
            "image",
            HFImage()
        )
    )

    val_dataset_split = (
        val_dataset_split.cast_column(
            "image",
            HFImage()
        )
    )

    return (
        train_dataset_split,
        val_dataset_split
    )


# ============================================================
# CREATE DATALOADERS
# ============================================================

def create_dataloaders(
    train_dataset,
    val_dataset,
    test_dataset
):

    print()
    print("=" * 70)
    print("CREATING DATALOADERS")
    print("=" * 70)

    # --------------------------------------------------------
    # Transforms
    # --------------------------------------------------------

    train_transform = get_train_transform()

    eval_transform = get_eval_transform()

    # --------------------------------------------------------
    # PyTorch datasets
    # --------------------------------------------------------

    train_data = PlantDiseaseDataset(
        train_dataset,
        transform=train_transform
    )

    val_data = PlantDiseaseDataset(
        val_dataset,
        transform=eval_transform
    )

    test_data = PlantDiseaseDataset(
        test_dataset,
        transform=eval_transform
    )

    # --------------------------------------------------------
    # Training DataLoader
    # --------------------------------------------------------

    train_loader = DataLoader(
        train_data,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=True
    )

    # --------------------------------------------------------
    # Validation DataLoader
    # --------------------------------------------------------

    val_loader = DataLoader(
        val_data,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=True
    )

    # --------------------------------------------------------
    # Test DataLoader
    # --------------------------------------------------------

    test_loader = DataLoader(
        test_data,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=True
    )

    print()
    print(
        f"Training batches  : "
        f"{len(train_loader)}"
    )

    print(
        f"Validation batches: "
        f"{len(val_loader)}"
    )

    print(
        f"Test batches      : "
        f"{len(test_loader)}"
    )

    return (
        train_loader,
        val_loader,
        test_loader
    )


# ============================================================
# TRAIN ONE EPOCH
# ============================================================

def train_one_epoch(
    model,
    train_loader,
    criterion,
    optimizer
):

    model.train()

    running_loss = 0.0

    correct = 0
    total = 0

    progress_bar = tqdm(
        train_loader,
        desc="Training",
        leave=False
    )

    for images, labels in progress_bar:

        # ----------------------------------------------------
        # Move data to GPU
        # ----------------------------------------------------

        images = images.to(
            device,
            non_blocking=True
        )

        labels = labels.to(
            device,
            non_blocking=True
        )

        # ----------------------------------------------------
        # Clear gradients
        # ----------------------------------------------------

        optimizer.zero_grad()

        # ----------------------------------------------------
        # Forward pass
        # ----------------------------------------------------

        outputs = model(images)

        # ----------------------------------------------------
        # Loss
        # ----------------------------------------------------

        loss = criterion(
            outputs,
            labels
        )

        # ----------------------------------------------------
        # Backpropagation
        # ----------------------------------------------------

        loss.backward()

        # ----------------------------------------------------
        # Update weights
        # ----------------------------------------------------

        optimizer.step()

        # ----------------------------------------------------
        # Accumulate loss
        # ----------------------------------------------------

        running_loss += (
            loss.item() *
            images.size(0)
        )

        # ----------------------------------------------------
        # Predictions
        # ----------------------------------------------------

        predictions = outputs.argmax(
            dim=1
        )

        correct += (
            predictions == labels
        ).sum().item()

        total += labels.size(0)

        progress_bar.set_postfix(
            loss=f"{loss.item():.4f}"
        )

    epoch_loss = (
        running_loss / total
    )

    epoch_accuracy = (
        correct / total
    )

    return (
        epoch_loss,
        epoch_accuracy
    )


# ============================================================
# VALIDATION
# ============================================================

def validate(
    model,
    val_loader,
    criterion
):

    model.eval()

    running_loss = 0.0

    correct = 0
    total = 0

    progress_bar = tqdm(
        val_loader,
        desc="Validation",
        leave=False
    )

    with torch.no_grad():

        for images, labels in progress_bar:

            # ------------------------------------------------
            # Move data to GPU
            # ------------------------------------------------

            images = images.to(
                device,
                non_blocking=True
            )

            labels = labels.to(
                device,
                non_blocking=True
            )

            # ------------------------------------------------
            # Forward pass
            # ------------------------------------------------

            outputs = model(images)

            # ------------------------------------------------
            # Loss
            # ------------------------------------------------

            loss = criterion(
                outputs,
                labels
            )

            running_loss += (
                loss.item() *
                images.size(0)
            )

            # ------------------------------------------------
            # Predictions
            # ------------------------------------------------

            predictions = outputs.argmax(
                dim=1
            )

            correct += (
                predictions == labels
            ).sum().item()

            total += labels.size(0)

    epoch_loss = (
        running_loss / total
    )

    epoch_accuracy = (
        correct / total
    )

    return (
        epoch_loss,
        epoch_accuracy
    )


# ============================================================
# TRAIN MODEL
# ============================================================

def train_model(
    model,
    train_loader,
    val_loader,
    criterion,
    optimizer
):

    print()
    print("=" * 70)
    print("STARTING TRAINING")
    print("=" * 70)

    print()
    print(
        f"Device        : {device}"
    )

    print(
        f"Epochs        : {NUM_EPOCHS}"
    )

    print(
        f"Batch size    : {BATCH_SIZE}"
    )

    print(
        f"Learning rate : {LEARNING_RATE}"
    )

    print(
        f"Weight decay  : {WEIGHT_DECAY}"
    )

    # --------------------------------------------------------
    # Learning-rate scheduler
    # --------------------------------------------------------

    scheduler = (
        torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer,
            mode="min",
            factor=0.5,
            patience=2
        )
    )

    # --------------------------------------------------------
    # Best-model tracking
    # --------------------------------------------------------

    best_val_loss = float("inf")

    best_val_accuracy = 0.0

    epochs_without_improvement = 0

    # --------------------------------------------------------
    # Training history
    # --------------------------------------------------------

    history = {
        "train_loss": [],
        "train_accuracy": [],
        "val_loss": [],
        "val_accuracy": [],
        "learning_rate": []
    }

    # --------------------------------------------------------
    # Create model directory
    # --------------------------------------------------------

    os.makedirs(
        os.path.dirname(MODEL_PATH),
        exist_ok=True
    )

    # --------------------------------------------------------
    # Training loop
    # --------------------------------------------------------

    for epoch in range(
        1,
        NUM_EPOCHS + 1
    ):

        print()
        print("=" * 70)

        print(
            f"Epoch {epoch}/{NUM_EPOCHS}"
        )

        print("=" * 70)

        start_time = time.time()

        # ====================================================
        # TRAIN
        # ====================================================

        train_loss, train_accuracy = (
            train_one_epoch(
                model,
                train_loader,
                criterion,
                optimizer
            )
        )

        # ====================================================
        # VALIDATE
        # ====================================================

        val_loss, val_accuracy = (
            validate(
                model,
                val_loader,
                criterion
            )
        )

        # ====================================================
        # SCHEDULER
        # ====================================================

        scheduler.step(
            val_loss
        )

        current_lr = (
            optimizer.param_groups[0]["lr"]
        )

        # ====================================================
        # SAVE HISTORY
        # ====================================================

        history["train_loss"].append(
            train_loss
        )

        history["train_accuracy"].append(
            train_accuracy
        )

        history["val_loss"].append(
            val_loss
        )

        history["val_accuracy"].append(
            val_accuracy
        )

        history["learning_rate"].append(
            current_lr
        )

        # ====================================================
        # EPOCH TIME
        # ====================================================

        epoch_time = (
            time.time() - start_time
        )

        # ====================================================
        # PRINT METRICS
        # ====================================================

        print()

        print(
            f"Train Loss:          "
            f"{train_loss:.4f}"
        )

        print(
            f"Train Accuracy:      "
            f"{train_accuracy * 100:.2f}%"
        )

        print(
            f"Validation Loss:     "
            f"{val_loss:.4f}"
        )

        print(
            f"Validation Accuracy: "
            f"{val_accuracy * 100:.2f}%"
        )

        print(
            f"Learning Rate:       "
            f"{current_lr:.6f}"
        )

        print(
            f"Epoch Time:          "
            f"{epoch_time / 60:.2f} minutes"
        )

        # ====================================================
        # SAVE BEST MODEL
        # ====================================================

        if val_loss < best_val_loss:

            best_val_loss = val_loss

            best_val_accuracy = (
                val_accuracy
            )

            epochs_without_improvement = 0

            checkpoint = {

                "epoch": epoch,

                "model_state_dict":
                    model.state_dict(),

                "optimizer_state_dict":
                    optimizer.state_dict(),

                "val_loss":
                    val_loss,

                "val_accuracy":
                    val_accuracy,

                "history":
                    history
            }

            torch.save(
                checkpoint,
                MODEL_PATH
            )

            print()
            print(
                "✓ BEST MODEL SAVED"
            )

            print(
                f"  {MODEL_PATH}"
            )

        else:

            epochs_without_improvement += 1

            print()

            print(
                "No validation improvement: "
                f"{epochs_without_improvement}/"
                f"{EARLY_STOPPING_PATIENCE}"
            )

        # ====================================================
        # EARLY STOPPING
        # ====================================================

        if (
            epochs_without_improvement
            >= EARLY_STOPPING_PATIENCE
        ):

            print()
            print(
                "Early stopping triggered."
            )

            break

    # ========================================================
    # TRAINING SUMMARY
    # ========================================================

    print()
    print("=" * 70)
    print("TRAINING COMPLETE")
    print("=" * 70)

    print()

    print(
        f"Best Validation Loss: "
        f"{best_val_loss:.4f}"
    )

    print(
        f"Best Validation Accuracy: "
        f"{best_val_accuracy * 100:.2f}%"
    )

    print()

    print(
        "Best model saved at:"
    )

    print(
        MODEL_PATH
    )

    return history


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 70)
    print("PLANT DISEASE CNN TRAINING")
    print("=" * 70)

    # ========================================================
    # DEVICE INFORMATION
    # ========================================================

    print()

    print(
        f"PyTorch version : "
        f"{torch.__version__}"
    )

    print(
        f"Device          : "
        f"{device}"
    )

    if torch.cuda.is_available():

        print(
            f"GPU             : "
            f"{torch.cuda.get_device_name(0)}"
        )

        print(
            f"CUDA version    : "
            f"{torch.version.cuda}"
        )

    # ========================================================
    # LOAD OFFICIAL TRAIN / TEST DATA
    # ========================================================

    (
        official_train_dataset,
        official_test_dataset
    ) = load_plantvillage()

    # ========================================================
    # CREATE GROUP-AWARE TRAIN / VALIDATION SPLIT
    # ========================================================

    (
        train_dataset,
        val_dataset
    ) = create_train_validation_split(
        official_train_dataset
    )

    # ========================================================
    # CREATE DATALOADERS
    # ========================================================

    (
        train_loader,
        val_loader,
        test_loader
    ) = create_dataloaders(
        train_dataset,
        val_dataset,
        official_test_dataset
    )

    # ========================================================
    # CREATE CNN
    # ========================================================

    print()
    print("=" * 70)
    print("CREATING CNN MODEL")
    print("=" * 70)

    model = PlantDiseaseCNN(
        num_classes=NUM_CLASSES
    )

    model = model.to(device)

    # --------------------------------------------------------
    # Parameter count
    # --------------------------------------------------------

    total_parameters = sum(
        p.numel()
        for p in model.parameters()
    )

    trainable_parameters = sum(
        p.numel()
        for p in model.parameters()
        if p.requires_grad
    )

    print()

    print(
        f"Total parameters     : "
        f"{total_parameters:,}"
    )

    print(
        f"Trainable parameters : "
        f"{trainable_parameters:,}"
    )

    # ========================================================
    # LOSS
    # ========================================================

    criterion = nn.CrossEntropyLoss()

    # ========================================================
    # OPTIMIZER
    # ========================================================

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY
    )

    # ========================================================
    # TRAIN
    # ========================================================

    history = train_model(
        model,
        train_loader,
        val_loader,
        criterion,
        optimizer
    )

    # ========================================================
    # SAVE TRAINING HISTORY
    # ========================================================

    os.makedirs(
        os.path.dirname(HISTORY_PATH),
        exist_ok=True
    )

    torch.save(
        history,
        HISTORY_PATH
    )

    print()

    print(
        "Training history saved:"
    )

    print(
        HISTORY_PATH
    )

    # ========================================================
    # FINAL MESSAGE
    # ========================================================

    print()
    print("=" * 70)
    print("BASELINE CNN TRAINING FINISHED")
    print("=" * 70)

    print()

    print(
        "Best model:"
    )

    print(
        MODEL_PATH
    )

    print()

    print(
        "Training history:"
    )

    print(
        HISTORY_PATH
    )

    print()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()