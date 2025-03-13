from django.views.generic import TemplateView
import requests

class CommitPanelView(TemplateView):
    template_name = "custom_dashboard_plugin/commit_panel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Configura qui il repository GitHub
        repo_owner = "AngeloSor"
        repo_name = "custom_dashboard_plugin"
        github_api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        try:
            r = requests.get(github_api_url, timeout=5)
            if r.status_code == 200:
                commits = r.json()
                context["commits"] = commits[:10]  # prendi gli ultimi 10 commit
            else:
                context["error"] = f"GitHub API returned status code {r.status_code}"
        except Exception as e:
            context["error"] = str(e)
        return context
