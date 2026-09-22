function PlantInformation({ information }) {

  if (!information) {
    return null;
  }


  return (

    <section className="v4-information-card">

      <div className="v4-card-header">

        <div className="v4-card-icon">
          🌱
        </div>

        <div>

          <span className="v4-eyebrow">
            PLANT INFORMATION
          </span>

          <h2>
            {information.plant}
          </h2>

        </div>

      </div>


      <div className="v4-plant-grid">

        <div className="v4-info-item">

          <span>
            Plant
          </span>

          <strong>
            {information.plant}
          </strong>

        </div>


        <div className="v4-info-item">

          <span>
            Condition
          </span>

          <strong>
            {information.disease}
          </strong>

        </div>


        <div className="v4-info-item">

          <span>
            Category
          </span>

          <strong>
            {information.category}
          </strong>

        </div>

      </div>

    </section>

  );
}


export default PlantInformation;