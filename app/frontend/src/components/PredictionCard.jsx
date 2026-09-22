function formatClassName(className) {
  return className
    .replace(/___/g, " — ")
    .replace(/_/g, " ")
    .replace(/,\s*/g, ", ");
}

function PredictionCard({
  prediction,
  rank
}) {

  const percentage = (
    prediction.confidence * 100
  ).toFixed(2);

  return (
    <div
      className={`prediction-item ${
        rank === 1 ? "top-prediction" : ""
      }`}
    >

      <div className="prediction-rank">
        {rank}
      </div>

      <div className="prediction-info">

        <span className="prediction-name">
          {formatClassName(
            prediction.class_name
          )}
        </span>

        <div className="prediction-bar">
          <div
            className="prediction-bar-fill"
            style={{
              width: `${percentage}%`
            }}
          />
        </div>

      </div>

      <span className="prediction-confidence">
        {percentage}%
      </span>

    </div>
  );
}

export default PredictionCard;