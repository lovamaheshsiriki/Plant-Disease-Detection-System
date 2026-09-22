import { useLocation, useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";

import DiseaseExplanation from "../components/DiseaseExplanation";
import PlantInformation from "../components/PlantInformation";
import SymptomsCard from "../components/SymptomsCard";
import TreatmentCard from "../components/TreatmentCard";
import PreventionCard from "../components/PreventionCard";


function formatDiseaseName(name) {

  if (!name) {
    return "Unknown condition";
  }


  return name
    .replace(/___/g, " — ")
    .replace(/_/g, " ");
}


function Results() {

  const location =
    useLocation();

  const navigate =
    useNavigate();


  const result =
    location.state?.result;

  const imageUrl =
    location.state?.imageUrl;


  /*
   * ----------------------------------------------------------
   * No result
   * ----------------------------------------------------------
   */

  if (!result) {

    return (

      <div className="app-shell">

        <Navbar />

        <main className="results-page">

          <div className="empty-results">

            <div className="empty-results-icon">
              🌱
            </div>

            <h1>
              No analysis available
            </h1>

            <p>
              Please analyze a plant image first.
            </p>

            <button
              type="button"
              className="analyze-button"
              onClick={() =>
                navigate("/analyze")
              }
            >
              Analyze a plant →
            </button>

          </div>

        </main>

      </div>

    );

  }


  /*
   * ----------------------------------------------------------
   * Extract information
   * ----------------------------------------------------------
   */

  const information =
    result.disease_information;


  const confidence =
    Number(result.confidence || 0);


  const confidencePercent =
    (confidence * 100).toFixed(2);


  const predictedName =
    formatDiseaseName(
      result.predicted_class
    );


  const isHealthy =
    information?.category === "Healthy";


  /*
   * ----------------------------------------------------------
   * RENDER
   * ----------------------------------------------------------
   */

  return (

    <div className="app-shell">

      <Navbar />


      <main className="results-page">


        {/* ==================================================
            TOP RESULT
            ================================================== */}

        <div className="results-hero">


          {/* IMAGE */}

          <div className="results-image-card">

            {imageUrl ? (

              <img
                src={imageUrl}
                alt="Analyzed plant"
                className="results-image"
              />

            ) : (

              <div className="results-image-empty">
                🌿
              </div>

            )}


            <div className="image-status">

              <span className="status-dot" />

              Image analyzed successfully

            </div>

          </div>


          {/* PREDICTION */}

          <div className="results-summary">

            <div className="results-summary-top">

              <span className="eyebrow">
                PRIMARY PREDICTION
              </span>


              <span
                className={
                  isHealthy
                    ? "condition-badge healthy"
                    : "condition-badge"
                }
              >

                {isHealthy
                  ? "✓ Healthy"
                  : "⚠ Condition detected"
                }

              </span>

            </div>


            <h1>
              {predictedName}
            </h1>


            <div className="confidence-section">

              <div className="confidence-header">

                <span>
                  AI confidence
                </span>

                <strong>
                  {confidencePercent}%
                </strong>

              </div>


              <div className="confidence-bar">

                <div
                  className="confidence-fill"
                  style={{
                    width: `${Math.min(
                      confidence * 100,
                      100
                    )}%`
                  }}
                />

              </div>


              <div className="confidence-label">

                <span>
                  ✓
                </span>

                {confidence >= 0.8
                  ? "High confidence"
                  : confidence >= 0.6
                    ? "Moderate confidence"
                    : "Low confidence"}

              </div>

            </div>


            {/* IMAGE QUALITY */}

            {result.image_quality && (

              <div className="results-quality">

                <div>

                  <span>
                    Image quality
                  </span>

                  <strong>
                    {
                      result.image_quality.status
                    }
                  </strong>

                </div>


                <div>

                  <span>
                    Resolution
                  </span>

                  <strong>
                    {
                      result.image_quality
                        .resolution
                        .width
                    }{" "}
                    ×{" "}
                    {
                      result.image_quality
                        .resolution
                        .height
                    }
                  </strong>

                </div>


                <div>

                  <span>
                    Brightness
                  </span>

                  <strong>
                    {
                      Math.round(
                        result.image_quality
                          .brightness
                      )
                    }
                  </strong>

                </div>


                <div>

                  <span>
                    Sharpness
                  </span>

                  <strong>
                    {
                      Math.round(
                        result.image_quality
                          .sharpness
                      )
                    }
                  </strong>

                </div>

              </div>

            )}

          </div>

        </div>


        {/* ==================================================
            REAL WORLD WARNING
            ================================================== */}

        {result.real_world_warning && (

          <div className="real-world-warning">

            <span>
              ℹ
            </span>

            <p>
              {result.real_world_warning}
            </p>

          </div>

        )}


        {/* ==================================================
            V4 INFORMATION
            ================================================== */}

        {information && (

          <div className="v4-results-grid">


            <DiseaseExplanation
              information={information}
            />


            <PlantInformation
              information={information}
            />


            <SymptomsCard
              information={information}
            />


            <TreatmentCard
              information={information}
            />


            <PreventionCard
              information={information}
            />

          </div>

        )}


        {/* ==================================================
            ACTIONS
            ================================================== */}

        <div className="results-actions">

          <button
            type="button"
            className="secondary-result-button"
            onClick={() =>
              navigate("/analyze")
            }
          >
            ← Analyze another image
          </button>

        </div>


      </main>

    </div>

  );

}


export default Results;