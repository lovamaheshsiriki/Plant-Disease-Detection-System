function TreatmentCard({ information }) {

  if (!information) {
    return null;
  }


  return (

    <section className="v4-information-card treatment-card">

      <div className="v4-card-header">

        <div className="v4-card-icon treatment-icon">
          🧪
        </div>

        <div>

          <span className="v4-eyebrow">
            MANAGEMENT
          </span>

          <h2>
            What you can do
          </h2>

        </div>

      </div>


      <div className="v4-list">

        {information.management.map(
          (item, index) => (

            <div
              className="v4-list-item"
              key={index}
            >

              <span className="v4-number">
                {index + 1}
              </span>

              <span>
                {item}
              </span>

            </div>

          )
        )}

      </div>


      <div className="v4-treatment-note">

        <span>
          ⚠️
        </span>

        <p>
          Treatment depends on the crop,
          disease severity, local conditions,
          and applicable agricultural guidance.
          Follow approved product labels and
          local recommendations when chemical
          treatment is considered.
        </p>

      </div>

    </section>

  );
}


export default TreatmentCard;