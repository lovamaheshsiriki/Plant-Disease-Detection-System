function PreventionCard({ information }) {

  if (!information) {
    return null;
  }


  return (

    <section className="v4-information-card">

      <div className="v4-card-header">

        <div className="v4-card-icon">
          🛡️
        </div>

        <div>

          <span className="v4-eyebrow">
            PREVENTION
          </span>

          <h2>
            Reduce future risk
          </h2>

        </div>

      </div>


      <div className="v4-list">

        {information.prevention.map(
          (item, index) => (

            <div
              className="v4-list-item"
              key={index}
            >

              <span className="v4-check">
                ✓
              </span>

              <span>
                {item}
              </span>

            </div>

          )
        )}

      </div>

    </section>

  );
}


export default PreventionCard;