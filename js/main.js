async function loadRecordsStats() {
    try {
        const response = await fetch("device/output/stats.json");

        if (!response.ok) {
            throw new Error("stats.json을 불러올 수 없습니다.");
        }

        const stats = await response.json();

        const totalElement = document.getElementById("record-total");
        const typesElement = document.getElementById("record-types");

        if (totalElement) {
            totalElement.textContent = stats.total_days;
        }

        if (typesElement) {
            typesElement.textContent = stats.ability_count;
        }
    } catch (error) {
        console.error("기록 통계를 불러오지 못했습니다.", error);
    }
}

loadRecordsStats();
