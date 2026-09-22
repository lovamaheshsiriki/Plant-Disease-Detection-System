import { useRef, useState } from "react";

function ImageUploader({
  onImageSelect,
  selectedFile,
  previewUrl
}) {

  const inputRef = useRef(null);

  const [isDragging, setIsDragging] = useState(false);

  function handleFile(file) {

    if (!file) {
      return;
    }

    if (!file.type.startsWith("image/")) {
      alert("Please select an image file.");
      return;
    }

    onImageSelect(file);
  }

  function handleInputChange(event) {

    const file = event.target.files?.[0];

    handleFile(file);
  }

  function handleDrop(event) {

    event.preventDefault();

    setIsDragging(false);

    const file = event.dataTransfer.files?.[0];

    handleFile(file);
  }

  function openFilePicker() {
    inputRef.current?.click();
  }

  return (
    <div className="uploader-wrapper">

      <input
        ref={inputRef}
        type="file"
        accept="image/jpeg,image/png,image/webp"
        onChange={handleInputChange}
        hidden
      />

      {!selectedFile ? (

        <div
          className={`upload-box ${
            isDragging ? "dragging" : ""
          }`}
          onDragOver={(event) => {
            event.preventDefault();
            setIsDragging(true);
          }}
          onDragLeave={() => {
            setIsDragging(false);
          }}
          onDrop={handleDrop}
          onClick={openFilePicker}
        >

          <div className="upload-icon">
            🌱
          </div>

          <h3>
            Drop your plant image here
          </h3>

          <p>
            or click to browse from your device
          </p>

          <span className="upload-formats">
            JPG · PNG · WebP
          </span>

        </div>

      ) : (

        <div className="selected-image">

          <img
            src={previewUrl}
            alt="Selected plant"
          />

          <div className="selected-image-overlay">

            <button
              type="button"
              className="change-image-btn"
              onClick={openFilePicker}
            >
              Choose another image
            </button>

          </div>

        </div>

      )}

    </div>
  );
}

export default ImageUploader;