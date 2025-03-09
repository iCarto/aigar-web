(function () {
  const supabaseUrl = "https://xkvovmqvoywmbnhwtudi.supabase.co";
  const supabaseKey =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhrdm92bXF2b3l3bWJuaHd0dWRpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzcwMTY2MzMsImV4cCI6MjA1MjU5MjYzM30.HRDvlz3dZwD8jl5zW94h_qcuGl0evQuGWUHouuX4WaY";

  const spb = supabase.createClient(supabaseUrl, supabaseKey);
  const baseDomainPath = "/aigar-website/";
  const currentPath = window.location.pathname;

  const recordVisit = (url) => {
    if (localStorage.getItem(`counterInitialized-${url}`) === "true") {
      return;
    }

    spb
      .rpc("increment_page_visit", {
        page_url: url,
      })
      .then(({ data, error }) => {
        console.log("Visit recorded for url:", url);
        if (error) {
          console.log("Error al actualizar contador para url:", url, error);
          throw error;
        }
      })
      .catch((error) => {
        console.error("Error al actualizar contador para url:", url, error);
      });

    localStorage.setItem(`counterInitialized-${url}`, "true");
  };

  const initializeCounter = () => {
    recordVisit(baseDomainPath);
    recordVisit(currentPath);
  };

  const getVisitCount = () => {
    spb
      .from("page_visits")
      .select("visits")
      .eq("url", baseDomainPath)
      .single()
      .then(({ data, error }) => {
        console.log("Get visit count", { baseDomainPath, data });
        if (error) {
          console.error("Error al obtener contador:", error);
          throw error;
        }
        const counterElement = document.getElementById("page-views");
        if (counterElement) {
          counterElement.textContent = " " + data.visits;
        }
      })
      .catch((error) => {
        console.error("Error al obtener contador:", error);
      });
  };

  initializeCounter();
  getVisitCount();
})();
