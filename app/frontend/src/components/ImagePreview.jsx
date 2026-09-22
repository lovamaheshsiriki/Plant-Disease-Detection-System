function ImagePreview({
  imageUrl,
  alt = "Plant image"
}) {

  if (!imageUrl) {
    return null;
  }

  return (
    <div className="result-image-container">

      <img
        src={imageUrl}
        alt={alt}
        className="result-image"
      />

    </div>
  );
}

export default ImagePreview;