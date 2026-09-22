function SymptomsCard({ information }) {

  if (!information) {
    return null;
  }


  return (

    <section className="v4-information-card">

      <div className="v4-card-header">

        <div className="v4-card-icon">
          🔎
        </div>

        <div>

          <span className="v4-eyebrow">
            IDENTIFICATION GUIDE
          </span>

          <h2>
            Common symptoms
          </h2>

        </div>

      </div>


      <div className="v4-list">

        {information.symptoms.map(
          (symptom, index) => (

            <div
              className="v4-list-item"
              key={index}
            >

              <span className="v4-check">
                ✓
              </span>

              <span>
                {symptom}
              </span>

            </div>

          )
        )}

      </div>

    </section>

  );
}


export default SymptomsCard;