import os

import matplotlib.pyplot as plt


def plot_training_loss(
    history,
    save_dir="results/plots"
):
    """
    Plot training and validation loss.
    """

    os.makedirs(save_dir, exist_ok=True)

    epochs = range(
        1,
        len(history["train_loss"]) + 1
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        epochs,
        history["train_loss"],
        label="Training Loss"
    )

    plt.plot(
        epochs,
        history["val_loss"],
        label="Validation Loss"
    )

    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training and Validation Loss")

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    save_path = os.path.join(
        save_dir,
        "training_loss.png"
    )

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return save_path


def plot_training_accuracy(
    history,
    save_dir="results/plots"
):
    """
    Plot training and validation accuracy.
    """

    os.makedirs(save_dir, exist_ok=True)

    epochs = range(
        1,
        len(history["train_accuracy"]) + 1
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        epochs,
        [x * 100 for x in history["train_accuracy"]],
        label="Training Accuracy"
    )

    plt.plot(
        epochs,
        [x * 100 for x in history["val_accuracy"]],
        label="Validation Accuracy"
    )

    plt.xlabel("Epoch")
    plt.ylabel("Accuracy (%)")
    plt.title("Training and Validation Accuracy")

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    save_path = os.path.join(
        save_dir,
        "training_accuracy.png"
    )

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return save_path


def plot_learning_rate(
    history,
    save_dir="results/plots"
):
    """
    Plot learning-rate changes during training.
    """

    os.makedirs(save_dir, exist_ok=True)

    epochs = range(
        1,
        len(history["learning_rate"]) + 1
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        epochs,
        history["learning_rate"],
        marker="o"
    )

    plt.xlabel("Epoch")
    plt.ylabel("Learning Rate")
    plt.title("Learning Rate During Training")

    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    save_path = os.path.join(
        save_dir,
        "learning_rate.png"
    )

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return save_path


def plot_training_history(
    history,
    save_dir="results/plots"
):
    """
    Generate all training-history plots.
    """

    loss_path = plot_training_loss(
        history,
        save_dir
    )

    accuracy_path = plot_training_accuracy(
        history,
        save_dir
    )

    learning_rate_path = plot_learning_rate(
        history,
        save_dir
    )

    print()
    print("=" * 70)
    print("TRAINING PLOTS SAVED")
    print("=" * 70)

    print()
    print(f"Loss plot:       {loss_path}")
    print(f"Accuracy plot:   {accuracy_path}")
    print(f"Learning-rate:   {learning_rate_path}")

    return {
        "loss": loss_path,
        "accuracy": accuracy_path,
        "learning_rate": learning_rate_path
    }