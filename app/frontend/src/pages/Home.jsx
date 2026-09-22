import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

function Home() {
  return (
    <div className="app-shell">

      <Navbar />

      <main>

        {/* HERO */}

        <section className="hero">

          <div className="hero-content">

            <div className="hero-badge">
              <span className="status-dot" />
              AI-powered plant health detection
            </div>

            <h1>
              Understand your
              <span> plants better.</span>
            </h1>

            <p className="hero-description">
              Upload a photo of a plant leaf and let
              our deep learning model analyze it for
              common plant diseases.
            </p>

            <div className="hero-actions">

              <Link
                to="/analyze"
                className="primary-button"
              >
                Analyze a Leaf
                <span>→</span>
              </Link>

              <a
                href="#how-it-works"
                className="secondary-button"
              >
                How it works
              </a>

            </div>

            <div className="hero-stats">

              <div>
                <strong>38</strong>
                <span>Plant conditions</span>
              </div>

              <div>
                <strong>97.85%</strong>
                <span>Test accuracy</span>
              </div>

              <div>
                <strong>AI</strong>
                <span>Deep learning</span>
              </div>

            </div>

          </div>

          <div className="hero-visual">

            <div className="hero-glow" />

            <div className="plant-card">

              <div className="plant-card-top">
                <span>LIVE ANALYSIS</span>
                <span className="live-dot" />
              </div>

              <div className="leaf-visual">
                🌿
              </div>

              <div className="scan-line" />

              <div className="analysis-chip">
                <span className="chip-icon">
                  ✓
                </span>

                <div>
                  <small>AI DETECTION</small>
                  <strong>Plant analysis ready</strong>
                </div>
              </div>

            </div>

          </div>

        </section>


        {/* HOW IT WORKS */}

        <section
          className="how-section"
          id="how-it-works"
        >

          <div className="section-title">

            <span className="eyebrow">
              SIMPLE PROCESS
            </span>

            <h2>
              From leaf to insight.
            </h2>

            <p>
              Three simple steps to analyze your plant.
            </p>

          </div>

          <div className="steps">

            <div className="step-card">

              <div className="step-number">
                01
              </div>

              <div className="step-icon">
                📷
              </div>

              <h3>
                Upload a photo
              </h3>

              <p>
                Choose a clear image of the plant
                leaf you want to analyze.
              </p>

            </div>

            <div className="step-card">

              <div className="step-number">
                02
              </div>

              <div className="step-icon">
                🧠
              </div>

              <h3>
                AI analysis
              </h3>

              <p>
                Our convolutional neural network
                analyzes visual patterns in the leaf.
              </p>

            </div>

            <div className="step-card">

              <div className="step-number">
                03
              </div>

              <div className="step-icon">
                🔬
              </div>

              <h3>
                Get your result
              </h3>

              <p>
                See the predicted condition and
                the model's top predictions.
              </p>

            </div>

          </div>

        </section>


        {/* SUPPORTED PLANTS */}

        <section className="plants-section">

          <div className="section-title">

            <span className="eyebrow">
              DATASET
            </span>

            <h2>
              Built for diverse crops.
            </h2>

            <p>
              The current model recognizes 38
              plant health categories.
            </p>

          </div>

          <div className="plant-tags">

            {[
              "Apple",
              "Blueberry",
              "Cherry",
              "Corn",
              "Grape",
              "Orange",
              "Peach",
              "Pepper",
              "Potato",
              "Raspberry",
              "Soybean",
              "Squash",
              "Strawberry",
              "Tomato"
            ].map((plant) => (

              <span
                key={plant}
                className="plant-tag"
              >
                🌱 {plant}
              </span>

            ))}

          </div>

        </section>


        {/* CTA */}

        <section className="final-cta">

          <div>

            <span className="eyebrow">
              READY TO TRY?
            </span>

            <h2>
              Check your plant with AI.
            </h2>

            <p>
              Upload a leaf image and see what
              our model detects.
            </p>

          </div>

          <Link
            to="/analyze"
            className="primary-button"
          >
            Start Analysis
            <span>→</span>
          </Link>

        </section>

      </main>

      <footer className="footer">
        <span>🌿 PlantAI</span>
        <span>
          AI-powered plant disease detection
        </span>
      </footer>

    </div>
  );
}

export default Home;