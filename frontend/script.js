fetch("http://127.0.0.1:5000/api/dashboard")
  .then(res => res.json())
  .then(data => {
    document.getElementById("total-users").innerText = data.total_users;
    document.getElementById("active-sessions").innerText = data.active_sessions;
    document.getElementById("security-status").innerText = data.security_status;
    document.getElementById("s3-usage").innerText = data.s3_usage;

    const activityList = document.getElementById("activity-list");
    activityList.innerHTML = "";
    data.recent_activities.forEach(item => {
      const li = document.createElement("li");
      li.innerText = item;
      activityList.appendChild(li);
    });

    const alertsList = document.getElementById("alerts-list");
    alertsList.innerHTML = "";
    data.alerts.forEach(alert => {
      const li = document.createElement("li");
      li.innerText = alert;
      alertsList.appendChild(li);
    });
  })
  .catch(err => console.error("Error loading dashboard data:", err));
