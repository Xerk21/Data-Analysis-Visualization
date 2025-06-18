import pandas as pd
import plotly.express as px
from jinja2 import Template

df = pd.read_csv("DataSet.csv")

summary = []
for col in df.columns:
    total = len(df)
    available = df[col].notnull().sum()
    missing = total - available
    pct_available = round((available / total) * 100, 2)
    pct_missing = round((missing / total) * 100, 2)

    summary.append({
        'field': col,
        'available': f"{available:,}",
        'missing': f"{missing:,}",
        'pct_available': pct_available,
        'pct_missing': pct_missing
    })

    html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>QA Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <style>.progress-bar { font-size: 12px; }</style>
</head>
<body>
<div class="container mt-4">
    <h2 class="text-center text-success">QA Data Completeness Dashboard</h2>
    <hr/>
    <table class="table table-bordered">
        <thead class="thead-dark">
            <tr><th>Field</th><th>Available</th><th>Missing</th><th>Progress</th></tr>
        </thead>
        <tbody>
            {% for row in summary %}
            <tr>
                <td><b>{{ row.field }}</b></td>
                <td>{{ row.available }}</td>
                <td>{{ row.missing }}</td>
                <td>
                    <div class="progress">
                        <div class="progress-bar bg-success" style="width:{{ row.pct_available }}%">
                            {{ row.pct_available }}% available
                        </div>
                        <div class="progress-bar bg-danger" style="width:{{ row.pct_missing }}%">
                            {{ row.pct_missing }}% missing
                        </div>
                    </div>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
</body>
</html>
"""


html = Template(html_template).render(summary=summary)
with open("qa_dashboard.html", "w") as f:
    f.write(html)

print("HTML QA dashboard generated: qa_dashboard.html")

