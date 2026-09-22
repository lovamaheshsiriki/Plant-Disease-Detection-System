const API_BASE_URL = "https://plant-disease-detection-system-otkv.onrender.com";

export async function predictPlantDisease(file) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    `${API_BASE_URL}/predict`,
    {
      method: "POST",
      body: formData
    }
  );

  if (!response.ok) {
    let errorMessage = "Prediction failed.";

    try {
      const errorData = await response.json();

      if (errorData.detail) {
        errorMessage = errorData.detail;
      }
    } catch {
      // Keep default error message
    }

    throw new Error(errorMessage);
  }

  return response.json();
}
