import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import ImageUploader from "../components/ImageUploader";
import LoadingState from "../components/LoadingState";
import CameraCapture from "../components/CameraCapture";

import { predictPlantDisease } from "../services/api";


function Analyze() {

  const navigate = useNavigate();


  // ==========================================================
  // STATE
  // ==========================================================

  const [selectedFile, setSelectedFile] =
    useState(null);

  const [previewUrl, setPreviewUrl] =
    useState(null);

  const [isAnalyzing, setIsAnalyzing] =
    useState(false);

  const [isCameraOpen, setIsCameraOpen] =
    useState(false);

  const [error, setError] =
    useState("");


  // ==========================================================
  // CLEANUP PREVIEW URL
  // ==========================================================

  useEffect(() => {

    return () => {

      if (previewUrl) {

        URL.revokeObjectURL(
          previewUrl
        );

      }

    };

  }, [previewUrl]);


  // ==========================================================
  // HANDLE IMAGE SELECTION
  // ==========================================================

  function handleImageSelect(file) {

    setError("");

    if (!file) {
      return;
    }


    // Revoke previous preview

    if (previewUrl) {

      URL.revokeObjectURL(
        previewUrl
      );

    }


    setSelectedFile(file);

    const url =
      URL.createObjectURL(file);

    setPreviewUrl(url);

  }


  // ==========================================================
  // OPEN CAMERA
  // ==========================================================

  function handleOpenCamera() {

    setError("");

    setIsCameraOpen(true);

  }


  // ==========================================================
  // CLOSE CAMERA
  // ==========================================================

  function handleCloseCamera() {

    setIsCameraOpen(false);

  }


  // ==========================================================
  // HANDLE CAMERA CAPTURE
  // ==========================================================

  function handleCameraCapture(file) {

    setIsCameraOpen(false);

    handleImageSelect(file);

  }


  // ==========================================================
  // ANALYZE IMAGE
  // ==========================================================

  async function handleAnalyze() {

    if (!selectedFile) {

      setError(
        "Please select or capture a plant image first."
      );

      return;
    }


    setIsAnalyzing(true);

    setError("");


    try {

      const result =
        await predictPlantDisease(
          selectedFile
        );


      navigate(
        "/results",
        {
          state: {
            result,
            imageUrl: previewUrl
          }
        }
      );


    } catch (err) {

      setError(
        err.message ||
        "Something went wrong during analysis."
      );

    } finally {

      setIsAnalyzing(false);

    }

  }


  // ==========================================================
  // RENDER
  // ==========================================================

  return (

    <div className="app-shell">

      <Navbar />


      <main className="analyze-page">


        {/* ==================================================
            PAGE HEADER
            ================================================== */}

        <div className="page-heading">

          <span className="eyebrow">
            AI PLANT ANALYSIS
          </span>


          <h1>
            Analyze your plant
          </h1>


          <p>
            Upload a clear photo or use your
            camera to analyze a plant leaf.
          </p>

        </div>


        {/* ==================================================
            MAIN ANALYSIS CONTAINER
            ================================================== */}

        <div className="analyze-container">


          <div className="analyze-card">


            {!isAnalyzing ? (

              <>


                {/* ==========================================
                    IMAGE UPLOADER
                    ========================================== */}

                <ImageUploader
                  onImageSelect={
                    handleImageSelect
                  }

                  selectedFile={
                    selectedFile
                  }

                  previewUrl={
                    previewUrl
                  }
                />


                {/* ==========================================
                    CAMERA OPTION
                    ========================================== */}

                {!selectedFile && (

                  <div className="camera-option">


                    <div className="camera-divider">

                      <span />

                      <small>
                        OR
                      </small>

                      <span />

                    </div>


                    <button
                      type="button"
                      className="camera-open-button"
                      onClick={
                        handleOpenCamera
                      }
                    >

                      <span className="camera-button-icon">
                        📷
                      </span>

                      <span>
                        Take a photo
                      </span>

                    </button>


                    <p className="camera-help-text">
                      Use your device camera
                      to capture a plant leaf.
                    </p>

                  </div>

                )}


                {/* ==========================================
                    ERROR
                    ========================================== */}

                {error && (

                  <div className="error-message">

                    ⚠️ {error}

                  </div>

                )}


                {/* ==========================================
                    ANALYZE BUTTON
                    ========================================== */}

                <button
                  type="button"
                  className="analyze-button"
                  disabled={!selectedFile}
                  onClick={
                    handleAnalyze
                  }
                >

                  <span>
                    🧠
                  </span>

                  Analyze with AI

                  <span>
                    →
                  </span>

                </button>


              </>

            ) : (

              <LoadingState />

            )}

          </div>


          {/* =================================================
              TIPS
              ================================================= */}

          <div className="analysis-tips">

            <h3>
              📸 Tips for better results
            </h3>


            <ul>

              <li>
                Use a clear, focused image.
              </li>

              <li>
                Make sure the leaf is visible.
              </li>

              <li>
                Avoid very dark photographs.
              </li>

              <li>
                Try to capture the affected area.
              </li>

              <li>
                Keep the leaf inside the
                camera frame when capturing.
              </li>

            </ul>

          </div>


        </div>

      </main>


      {/* ====================================================
          CAMERA MODAL
          ==================================================== */}

      {isCameraOpen && (

        <CameraCapture
          onCapture={
            handleCameraCapture
          }

          onClose={
            handleCloseCamera
          }
        />

      )}

    </div>

  );

}


export default Analyze;