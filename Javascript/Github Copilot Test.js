function calculateBetweenDays(startDate, endDate) {
    var start = new Date(startDate);
    var end = new Date(endDate);
    var days = (end - start) / (1000 * 60 * 60 * 24);
    return days;
}