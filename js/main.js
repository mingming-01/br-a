async function loadRecordsStats() {
    try {
        const response = await fetch("device/output/stats.json", { cache: "no-store" });

        if (!response.ok) {
            throw new Error("stats.json을 불러올 수 없습니다.");
        }

        const stats = await response.json();

        const totalElement = document.getElementById("record-total");
        const practicedElement = document.getElementById("record-practiced");
        const partialElement = document.getElementById("record-partial");
        const noteElement = document.getElementById("record-note");

        if (totalElement) {
            totalElement.textContent = stats.total_days;
        }

        if (practicedElement) {
            practicedElement.textContent = stats.practice_completed_days;
        }

        if (partialElement) {
            partialElement.textContent = stats.practice_partial_days;
        }

        if (noteElement) {
            noteElement.textContent =
                `집계 범위: ${stats.period_start} ~ ${stats.period_end} · 마감 기록 ${stats.completed_days}일 · 진행 중 ${stats.in_progress_days}일`;
        }
    } catch (error) {
        console.error("기록 통계를 불러오지 못했습니다.", error);
    }
}

loadRecordsStats();
