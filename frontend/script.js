// Mock backend API call (replace with real Flask endpoint later)
const fetchDashboardData = async () => {
    return {
        totalUsers: 150,
        activeSessions: 42,
        securityStatus: "Safe",
        s3Usage: "12 GB",
        activities: [
            "User John logged in",
            "Admin updated permissions",
            "New EC2 instance launched"
        ],
        alerts: [
            "Suspicious login detected",
            "High CPU usage on server"
        ],
        sessionTrend: [5, 10, 8, 15, 20, 18, 25]
    };
};

// Update dashboard dynamically
fetchDashboardData().then(data => {
    document.getElementById("total-users").textContent = data.totalUsers;
    document.getElementById("active-sessions").textContent = data.activeSessions;

    let statusEl = document.getElementById("security-status");
    statusEl.textContent = data.securityStatus;
    statusEl.className = data.securityStatus.toLowerCase();

    document.getElementById("s3-usage").textContent = data.s3Usage;

    let activityList = document.getElementById("activity-list");
    activityList.innerHTML = "";
    data.activities.forEach(a => {
        let li = document.createElement("li");
        li.textContent = a;
        activityList.appendChild(li);
    });

    let alertsList = document.getElementById("alerts-list");
    alertsList.innerHTML = "";
    data.alerts.forEach(a => {
        let li = document.createElement("li");
        li.textContent = a;
        alertsList.appendChild(li);
    });

    // Chart
    const ctx = document.getElementById('sessionsChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
            datasets: [{
                label: 'Active Sessions',
                data: data.sessionTrend,
                backgroundColor: 'rgba(26,115,232,0.2)',
                borderColor: 'rgba(26,115,232,1)',
                borderWidth: 2,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            }
        }
    });
});
