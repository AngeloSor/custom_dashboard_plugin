# Lo slug deve corrispondere a quello definito in commit_panel.py
PANEL = 'commit_panel'
# Specifica il dashboard in cui vuoi che appaia (usa lo slug, in questo caso 'project')
PANEL_DASHBOARD = 'project'
# Se non usi gruppi particolari, puoi usare 'default'
PANEL_GROUP = 'default'
# Percorso completo alla classe del pannello
ADD_PANEL = 'custom_dashboard_plugin.panels.commit_panel.CommitPanel'
# IMPORTANTISSIMO: Registra anche le URL del plugin
ADD_URLS = 'custom_dashboard_plugin.urls'
