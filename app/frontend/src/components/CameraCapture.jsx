import {
  useEffect,
  useRef,
  useState
} from "react";


function CameraCapture({
  onCapture,
  onClose
}) {

  const videoRef =
    useRef(null);

  const canvasRef =
    useRef(null);

  const streamRef =
    useRef(null);

  const capturedUrlRef =
    useRef(null);


  const [error, setError] =
    useState("");

  const [isReady, setIsReady] =
    useState(false);

  const [capturedFile, setCapturedFile] =
    useState(null);

  const [capturedPreview, setCapturedPreview] =
    useState(null);


  /*
   * ==========================================================
   * ATTACH STREAM TO VIDEO
   * ==========================================================
   */

  async function attachStreamToVideo() {

    const video =
      videoRef.current;

    const stream =
      streamRef.current;


    if (!video || !stream) {
      return;
    }


    try {

      video.srcObject = stream;

      await video.play();

      /*
       * Some browsers need a small delay
       * before video dimensions become available.
       */

      if (
        video.videoWidth > 0 &&
        video.videoHeight > 0
      ) {

        setIsReady(true);

      }

    } catch (err) {

      console.error(
        "Unable to attach camera stream:",
        err
      );

      setIsReady(false);

    }

  }


  /*
   * ==========================================================
   * START CAMERA
   * ==========================================================
   */

  useEffect(() => {

    let mounted = true;


    async function startCamera() {

      try {

        setError("");

        setIsReady(false);


        /*
         * Request camera
         */

        const stream =
          await navigator.mediaDevices.getUserMedia({

            video: {

              facingMode: {
                ideal: "environment"
              },

              width: {
                ideal: 1280
              },

              height: {
                ideal: 720
              }

            },

            audio: false

          });


        /*
         * Component may have been closed
         * while camera permission was loading.
         */

        if (!mounted) {

          stream
            .getTracks()
            .forEach(
              (track) => track.stop()
            );

          return;

        }


        streamRef.current =
          stream;


        /*
         * Attach stream to current video
         */

        await attachStreamToVideo();


      } catch (err) {

        console.error(
          "Camera error:",
          err
        );


        if (!mounted) {
          return;
        }


        setError(
          "Unable to access the camera. " +
          "Please allow camera permission " +
          "and try again."
        );

        setIsReady(false);

      }

    }


    startCamera();


    /*
     * ========================================================
     * CLEANUP
     * ========================================================
     */

    return () => {

      mounted = false;

      stopCamera();

      revokeCapturedPreview();

    };

  }, []);


  /*
   * ==========================================================
   * REATTACH CAMERA AFTER RETAKE
   * ==========================================================
   *
   * IMPORTANT:
   *
   * When capturedPreview changes:
   *
   * true  -> captured image
   * false -> <video> created again
   *
   * The existing MediaStream must be attached
   * to the new video element.
   *
   * ==========================================================
   */

  useEffect(() => {

    if (!capturedPreview) {

      /*
       * Give React time to create
       * the new <video> element.
       */

      const timer =
        setTimeout(() => {

          attachStreamToVideo();

        }, 0);


      return () => {
        clearTimeout(timer);
      };

    }

  }, [capturedPreview]);


  /*
   * ==========================================================
   * VIDEO METADATA READY
   * ==========================================================
   */

  function handleVideoMetadata() {

    const video =
      videoRef.current;


    if (!video) {
      return;
    }


    if (
      video.videoWidth > 0 &&
      video.videoHeight > 0
    ) {

      setIsReady(true);

      setError("");

    }

  }


  /*
   * ==========================================================
   * STOP CAMERA
   * ==========================================================
   */

  function stopCamera() {

    if (streamRef.current) {

      streamRef.current
        .getTracks()
        .forEach(
          (track) => track.stop()
        );

      streamRef.current = null;

    }


    if (videoRef.current) {

      videoRef.current.srcObject =
        null;

    }


    setIsReady(false);

  }


  /*
   * ==========================================================
   * REVOKE CAPTURE PREVIEW
   * ==========================================================
   */

  function revokeCapturedPreview() {

    if (capturedUrlRef.current) {

      URL.revokeObjectURL(
        capturedUrlRef.current
      );

      capturedUrlRef.current =
        null;

    }

  }


  /*
   * ==========================================================
   * CAPTURE IMAGE
   * ==========================================================
   */

  function captureImage() {

    const video =
      videoRef.current;

    const canvas =
      canvasRef.current;


    if (!video || !canvas) {
      return;
    }


    /*
     * Make sure camera is actually ready.
     */

    if (
      !video.videoWidth ||
      !video.videoHeight
    ) {

      setError(
        "Camera is not ready yet. " +
        "Please wait a moment and try again."
      );

      return;

    }


    const width =
      video.videoWidth;

    const height =
      video.videoHeight;


    canvas.width =
      width;

    canvas.height =
      height;


    const context =
      canvas.getContext("2d");


    context.drawImage(
      video,
      0,
      0,
      width,
      height
    );


    canvas.toBlob(

      (blob) => {

        if (!blob) {

          setError(
            "Unable to capture the image."
          );

          return;

        }


        /*
         * Create File
         */

        const file =
          new File(
            [blob],
            `plant-capture-${Date.now()}.jpg`,
            {
              type: "image/jpeg"
            }
          );


        /*
         * Remove previous preview URL
         */

        revokeCapturedPreview();


        /*
         * Create new preview
         */

        const previewUrl =
          URL.createObjectURL(
            blob
          );


        capturedUrlRef.current =
          previewUrl;


        setCapturedFile(file);

        setCapturedPreview(
          previewUrl
        );

        setError("");

      },

      "image/jpeg",

      0.92

    );

  }


  /*
   * ==========================================================
   * RETAKE
   * ==========================================================
   */

  function handleRetake() {

    /*
     * IMPORTANT:
     *
     * Do NOT stop the camera here.
     *
     * We want to reuse the existing
     * camera stream.
     */

    revokeCapturedPreview();


    setCapturedFile(
      null
    );

    setCapturedPreview(
      null
    );

    setError("");

    setIsReady(false);

  }


  /*
   * ==========================================================
   * USE PHOTO
   * ==========================================================
   */

  function handleUsePhoto() {

    if (!capturedFile) {
      return;
    }


    /*
     * Stop camera only when
     * the user is finished with it.
     */

    stopCamera();

    revokeCapturedPreview();


    onCapture(
      capturedFile
    );

  }


  /*
   * ==========================================================
   * CLOSE CAMERA
   * ==========================================================
   */

  function handleClose() {

    stopCamera();

    revokeCapturedPreview();

    onClose();

  }


  /*
   * ==========================================================
   * CAPTURED PHOTO VIEW
   * ==========================================================
   */

  if (capturedPreview) {

    return (

      <div className="camera-overlay">

        <div className="camera-panel">


          {/* =================================================
              HEADER
              ================================================= */}

          <div className="camera-header">

            <button
              type="button"
              className="camera-close"
              onClick={handleClose}
              aria-label="Close camera"
            >
              ×
            </button>


            <div>

              <span className="camera-eyebrow">
                PHOTO CAPTURED
              </span>

              <h2>
                Review your photo
              </h2>

            </div>

          </div>


          {/* =================================================
              CAPTURED IMAGE
              ================================================= */}

          <div className="captured-photo-view">

            <img
              src={capturedPreview}
              alt="Captured plant"
              className="captured-photo"
            />

          </div>


          {/* =================================================
              SUCCESS MESSAGE
              ================================================= */}

          <div className="captured-photo-info">

            <div className="captured-success-icon">
              ✓
            </div>


            <div>

              <strong>
                Photo captured successfully
              </strong>

              <p>
                Check that the leaf is clearly
                visible before continuing.
              </p>

            </div>

          </div>


          {/* =================================================
              ACTIONS
              ================================================= */}

          <div className="capture-review-actions">

            <button
              type="button"
              className="retake-button"
              onClick={handleRetake}
            >

              <span>
                ↻
              </span>

              Retake

            </button>


            <button
              type="button"
              className="use-photo-button"
              onClick={handleUsePhoto}
            >

              <span>
                ✓
              </span>

              Use Photo

            </button>

          </div>

        </div>

      </div>

    );

  }


  /*
   * ==========================================================
   * LIVE CAMERA VIEW
   * ==========================================================
   */

  return (

    <div className="camera-overlay">

      <div className="camera-panel">


        {/* =================================================
            HEADER
            ================================================= */}

        <div className="camera-header">

          <button
            type="button"
            className="camera-close"
            onClick={handleClose}
            aria-label="Close camera"
          >
            ×
          </button>


          <div>

            <span className="camera-eyebrow">
              CAMERA
            </span>

            <h2>
              Scan your plant
            </h2>

          </div>

        </div>


        {/* =================================================
            CAMERA VIEW
            ================================================= */}

        <div className="camera-view">

          <video
            ref={videoRef}
            className="camera-video"
            playsInline
            muted
            autoPlay
            onLoadedMetadata={
              handleVideoMetadata
            }
          />


          {/* CAMERA FRAME */}

          <div className="camera-frame">

            <span className="corner top-left" />

            <span className="corner top-right" />

            <span className="corner bottom-left" />

            <span className="corner bottom-right" />

          </div>


          {/* LOADING */}

          {!isReady && !error && (

            <div className="camera-loading">

              <div className="camera-spinner" />

              <p>
                Starting camera...
              </p>

            </div>

          )}


          {/* ERROR */}

          {error && (

            <div className="camera-error">

              <div className="camera-error-icon">
                ⚠
              </div>

              <p>
                {error}
              </p>

            </div>

          )}

        </div>


        {/* =================================================
            INSTRUCTIONS
            ================================================= */}

        <div className="camera-instructions">

          <p>
            Position the plant leaf clearly
            inside the frame.
          </p>

          <span>
            Good lighting gives better results.
          </span>

        </div>


        {/* =================================================
            CAPTURE BUTTON
            ================================================= */}

        <div className="camera-controls">

          <button
            type="button"
            className="capture-button"
            onClick={captureImage}
            disabled={!isReady}
            aria-label="Capture image"
          >

            <span className="capture-button-inner" />

          </button>

        </div>


        {/* =================================================
            HIDDEN CANVAS
            ================================================= */}

        <canvas
          ref={canvasRef}
          style={{
            display: "none"
          }}
        />

      </div>

    </div>

  );

}


export default CameraCapture;