from pathlib import Path
import sys

import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from torch.utils.data import DataLoader
from datasets import load_dataset, Image as HFImage
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
from tqdm import tqdm


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# PROJECT IMPORTS
# ============================================================

from src.data.dataset import PlantDiseaseDataset
from src.data.preprocessing import get_eval_transform
from src.models.cnn import PlantDiseaseCNN


# ============================================================
# CONFIGURATION
# ============================================================

DATASET_NAME = "geraldmc/plantvillage-full"
DATASET_REVISION = "v0.1.0"

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "baseline_cnn_best.pth"
)

METRICS_DIR = (
    PROJECT_ROOT
    / "results"
    / "metrics"
)

CONFUSION_MATRIX_DIR = (
    PROJECT_ROOT
    / "results"
    / "confusion_matrix"
)

BATCH_SIZE = 32
NUM_CLASSES = 38


# ============================================================
# DEVICE
# ============================================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("PLANT DISEASE CNN - BASELINE EVALUATION")
    print("=" * 70)

    print()
    print("Device:", DEVICE)

    if torch.cuda.is_available():
        print(
            "GPU:",
            torch.cuda.get_device_name(0)
        )

        print(
            "CUDA:",
            torch.version.cuda
        )

    # --------------------------------------------------------
    # CREATE OUTPUT DIRECTORIES
    # --------------------------------------------------------

    METRICS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    CONFUSION_MATRIX_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # CHECK MODEL
    # --------------------------------------------------------

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            f"\nModel checkpoint not found:\n{MODEL_PATH}"
        )

    print()
    print("Model checkpoint:")
    print(MODEL_PATH)

    # --------------------------------------------------------
    # LOAD DATASET
    # --------------------------------------------------------

    print()
    print("Loading PlantVillage dataset...")

    dataset_dict = load_dataset(
        DATASET_NAME,
        revision=DATASET_REVISION
    )

    dataset = dataset_dict["train"]

    print(
        "Total images:",
        len(dataset)
    )

    # --------------------------------------------------------
    # SELECT OFFICIAL TEST SET
    # --------------------------------------------------------

    test_dataset = dataset.filter(
        lambda example:
        example["split"] == "test"
    )

    print(
        "Official test images:",
        len(test_dataset)
    )

    # --------------------------------------------------------
    # GET CLASS NAMES
    # --------------------------------------------------------

    class_df = dataset.select_columns(
        [
            "class_idx",
            "class_label"
        ]
    ).to_pandas()

    class_df = (
        class_df
        .drop_duplicates()
        .sort_values("class_idx")
    )

    class_names = (
        class_df["class_label"]
        .tolist()
    )

    if len(class_names) != NUM_CLASSES:

        raise ValueError(
            f"Expected {NUM_CLASSES} classes, "
            f"but found {len(class_names)}."
        )

    print(
        "Number of classes:",
        len(class_names)
    )

    # --------------------------------------------------------
    # RESTORE IMAGE FEATURE
    # --------------------------------------------------------

    test_dataset = test_dataset.cast_column(
        "image",
        HFImage()
    )

    # --------------------------------------------------------
    # PYTORCH DATASET
    # --------------------------------------------------------

    test_transform = get_eval_transform()

    test_data = PlantDiseaseDataset(
        test_dataset,
        transform=test_transform
    )

    # --------------------------------------------------------
    # DATALOADER
    # --------------------------------------------------------

    test_loader = DataLoader(
        test_data,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=0,
        pin_memory=True
    )

    print(
        "Test batches:",
        len(test_loader)
    )

    # --------------------------------------------------------
    # LOAD MODEL
    # --------------------------------------------------------

    print()
    print("Loading model...")

    model = PlantDiseaseCNN(
        num_classes=NUM_CLASSES
    )

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=DEVICE,
        weights_only=False
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.to(DEVICE)

    model.eval()

    print("Model loaded successfully.")

    if "epoch" in checkpoint:

        print(
            "Best epoch:",
            checkpoint["epoch"]
        )

    if "val_loss" in checkpoint:

        print(
            f"Validation loss: "
            f"{checkpoint['val_loss']:.4f}"
        )

    if "val_accuracy" in checkpoint:

        print(
            f"Validation accuracy: "
            f"{checkpoint['val_accuracy'] * 100:.2f}%"
        )

    # ========================================================
    # INFERENCE
    # ========================================================

    print()
    print("Running inference on official test set...")

    all_predictions = []
    all_labels = []

    with torch.inference_mode():

        progress_bar = tqdm(
            test_loader,
            total=len(test_loader),
            desc="Evaluating",
            unit="batch"
        )

        for images, labels in progress_bar:

            images = images.to(
                DEVICE,
                non_blocking=True
            )

            labels = labels.to(
                DEVICE,
                non_blocking=True
            )

            outputs = model(images)

            predictions = torch.argmax(
                outputs,
                dim=1
            )

            all_predictions.append(
                predictions.cpu()
            )

            all_labels.append(
                labels.cpu()
            )

    # --------------------------------------------------------
    # COMBINE BATCH RESULTS
    # --------------------------------------------------------

    y_pred = torch.cat(
        all_predictions
    ).numpy()

    y_true = torch.cat(
        all_labels
    ).numpy()

    print()
    print("Inference completed.")

    print(
        "Total predictions:",
        len(y_pred)
    )

    # ========================================================
    # BASIC VALIDATION
    # ========================================================

    if len(y_true) != len(y_pred):

        raise RuntimeError(
            "Number of predictions does not "
            "match number of labels."
        )

    if len(y_true) != len(test_dataset):

        raise RuntimeError(
            "Number of predictions does not "
            "match test dataset size."
        )

    # ========================================================
    # OVERALL METRICS
    # ========================================================

    print()
    print("=" * 70)
    print("CALCULATING TEST METRICS")
    print("=" * 70)

    # Accuracy
    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    print(
        "✓ Accuracy calculated"
    )

    # Macro Precision
    precision_macro = precision_score(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        average="macro",
        zero_division=0
    )

    print(
        "✓ Macro precision calculated"
    )

    # Macro Recall
    recall_macro = recall_score(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        average="macro",
        zero_division=0
    )

    print(
        "✓ Macro recall calculated"
    )

    # Macro F1
    f1_macro = f1_score(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        average="macro",
        zero_division=0
    )

    print(
        "✓ Macro F1 calculated"
    )

    # Weighted Precision
    precision_weighted = precision_score(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        average="weighted",
        zero_division=0
    )

    print(
        "✓ Weighted precision calculated"
    )

    # Weighted Recall
    recall_weighted = recall_score(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        average="weighted",
        zero_division=0
    )

    print(
        "✓ Weighted recall calculated"
    )

    # Weighted F1
    f1_weighted = f1_score(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        average="weighted",
        zero_division=0
    )

    print(
        "✓ Weighted F1 calculated"
    )

    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

    print()
    print("=" * 70)
    print("OVERALL TEST RESULTS")
    print("=" * 70)

    print(
        f"Test samples       : {len(y_true)}"
    )

    print(
        f"Accuracy            : "
        f"{accuracy * 100:.2f}%"
    )

    print(
        f"Macro Precision     : "
        f"{precision_macro:.4f}"
    )

    print(
        f"Macro Recall        : "
        f"{recall_macro:.4f}"
    )

    print(
        f"Macro F1            : "
        f"{f1_macro:.4f}"
    )

    print(
        f"Weighted Precision  : "
        f"{precision_weighted:.4f}"
    )

    print(
        f"Weighted Recall     : "
        f"{recall_weighted:.4f}"
    )

    print(
        f"Weighted F1         : "
        f"{f1_weighted:.4f}"
    )

    # ========================================================
    # CLASSIFICATION REPORT
    # ========================================================

    print()
    print("=" * 70)
    print("GENERATING PER-CLASS REPORT")
    print("=" * 70)

    report = classification_report(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        target_names=class_names,
        digits=4,
        zero_division=0
    )

    print()
    print(report)

    # ========================================================
    # SAVE CLASSIFICATION REPORT
    # ========================================================

    report_path = (
        METRICS_DIR
        / "baseline_classification_report.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "PLANT DISEASE CNN - TEST EVALUATION\n"
        )

        file.write(
            "=" * 70 + "\n\n"
        )

        file.write(
            f"Test samples: {len(y_true)}\n"
        )

        file.write(
            f"Accuracy: {accuracy:.4f}\n"
        )

        file.write(
            f"Macro Precision: "
            f"{precision_macro:.4f}\n"
        )

        file.write(
            f"Macro Recall: "
            f"{recall_macro:.4f}\n"
        )

        file.write(
            f"Macro F1: "
            f"{f1_macro:.4f}\n"
        )

        file.write(
            f"Weighted Precision: "
            f"{precision_weighted:.4f}\n"
        )

        file.write(
            f"Weighted Recall: "
            f"{recall_weighted:.4f}\n"
        )

        file.write(
            f"Weighted F1: "
            f"{f1_weighted:.4f}\n\n"
        )

        file.write(
            "PER-CLASS CLASSIFICATION REPORT\n"
        )

        file.write(
            "=" * 70 + "\n\n"
        )

        file.write(report)

    print()
    print(
        "Classification report saved:"
    )

    print(
        report_path
    )

    # ========================================================
    # SAVE OVERALL METRICS CSV
    # ========================================================

    metrics = {
        "test_samples": len(y_true),
        "accuracy": accuracy,
        "macro_precision": precision_macro,
        "macro_recall": recall_macro,
        "macro_f1": f1_macro,
        "weighted_precision": precision_weighted,
        "weighted_recall": recall_weighted,
        "weighted_f1": f1_weighted,
    }

    metrics_df = pd.DataFrame(
        [metrics]
    )

    metrics_path = (
        METRICS_DIR
        / "baseline_test_metrics.csv"
    )

    metrics_df.to_csv(
        metrics_path,
        index=False
    )

    print(
        "Overall metrics saved:"
    )

    print(
        metrics_path
    )

    # ========================================================
    # CONFUSION MATRIX
    # ========================================================

    print()
    print("=" * 70)
    print("GENERATING CONFUSION MATRIX")
    print("=" * 70)

    cm = confusion_matrix(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES))
    )

    plt.figure(
        figsize=(20, 18)
    )

    plt.imshow(
        cm,
        interpolation="nearest"
    )

    plt.title(
        "Plant Disease CNN - Confusion Matrix"
    )

    plt.colorbar()

    tick_marks = np.arange(
        NUM_CLASSES
    )

    plt.xticks(
        tick_marks,
        class_names,
        rotation=90,
        fontsize=7
    )

    plt.yticks(
        tick_marks,
        class_names,
        fontsize=7
    )

    plt.xlabel(
        "Predicted Class"
    )

    plt.ylabel(
        "True Class"
    )

    plt.tight_layout()

    confusion_matrix_path = (
        CONFUSION_MATRIX_DIR
        / "baseline_confusion_matrix.png"
    )

    plt.savefig(
        confusion_matrix_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        "Confusion matrix image saved:"
    )

    print(
        confusion_matrix_path
    )

    # ========================================================
    # SAVE CONFUSION MATRIX CSV
    # ========================================================

    cm_df = pd.DataFrame(
        cm,
        index=class_names,
        columns=class_names
    )

    cm_csv_path = (
        CONFUSION_MATRIX_DIR
        / "baseline_confusion_matrix.csv"
    )

    cm_df.to_csv(
        cm_csv_path
    )

    print(
        "Confusion matrix CSV saved:"
    )

    print(
        cm_csv_path
    )

    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print()
    print("=" * 70)
    print("EVALUATION COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print()
    print(
        f"Test Accuracy : {accuracy * 100:.2f}%"
    )

    print(
        f"Macro F1      : {f1_macro:.4f}"
    )

    print(
        f"Weighted F1   : {f1_weighted:.4f}"
    )

    print()
    print("Output files:")
    print()
    print(
        f"1. {metrics_path}"
    )

    print(
        f"2. {report_path}"
    )

    print(
        f"3. {confusion_matrix_path}"
    )

    print(
        f"4. {cm_csv_path}"
    )

    print()
    print("=" * 70)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()