function DiseaseExplanation({ information }) {

  if (!information) {
    return null;
  }


  return (

    <section className="v4-information-card">

      <div className="v4-card-header">

        <div className="v4-card-icon">
          💡
        </div>

        <div>

          <span className="v4-eyebrow">
            AI EXPLANATION
          </span>

          <h2>
            What does this mean?
          </h2>

        </div>

      </div>


      <p className="v4-description">
        {information.description}
      </p>


      <div className="v4-category">

        <span>
          Disease category
        </span>

        <strong>
          {information.category}
        </strong>

      </div>

    </section>

  );
}


export default DiseaseExplanation;