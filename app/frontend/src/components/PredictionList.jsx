import PredictionCard from "./PredictionCard";

function PredictionList({
  predictions
}) {

  return (
    <section className="prediction-list">

      <div className="section-heading">
        <span>AI Predictions</span>

        <small>
          Top {predictions.length}
        </small>
      </div>

      <div className="predictions">

        {predictions.map(
          (prediction, index) => (
            <PredictionCard
              key={prediction.class_name}
              prediction={prediction}
              rank={index + 1}
            />
          )
        )}

      </div>

    </section>
  );
}

export default PredictionList;