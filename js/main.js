async function verifyRecordsSource() {
    const noteElement = document.getElementById("record-note");
    if (!noteElement) return;

    const pendingMessage =
        "날짜별 기록과 집계 요약의 날짜·건수 차이를 확인해 공개 수치를 재검증하고 있습니다.";
    noteElement.textContent = pendingMessage;

    try {
        const [summaryResponse, daysResponse] = await Promise.all([
            fetch("device/input/ritual-summary.json", { cache: "no-store" }),
            fetch("device/input/ritual-days.json", { cache: "no-store" })
        ]);

        if (!summaryResponse.ok || !daysResponse.ok) {
            throw new Error("기록 원본 파일을 불러오지 못했습니다.");
        }

        const [summary, days] = await Promise.all([
            summaryResponse.json(),
            daysResponse.json()
        ]);

        const dates = [...new Set(days.map((day) => day.date).filter(Boolean))].sort();
        const completed = days.filter((day) => day.status === "completed");
        const inProgress = days.filter((day) => day.status === "in_progress");
        const practiced = completed.filter((day) => day.practice_status === "실천했다").length;
        const partial = completed.filter((day) => day.practice_status === "일부 실천했다").length;

        const isConsistent =
            dates.length === summary.total_days &&
            dates[0] === summary.period_start &&
            dates[dates.length - 1] === summary.period_end &&
            completed.length === summary.completed_days &&
            inProgress.length === summary.in_progress_days &&
            practiced === summary.practice_completed_days &&
            partial === summary.practice_partial_days;

        noteElement.textContent = isConsistent
            ? "날짜별 기록과 집계 요약이 일치합니다. 공개 수치는 별도 검토 후 반영합니다."
            : pendingMessage;
    } catch (error) {
        noteElement.textContent = pendingMessage;
        console.error("기록 집계의 일관성을 확인하지 못했습니다.", error);
    }
}

verifyRecordsSource();
