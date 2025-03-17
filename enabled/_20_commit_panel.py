# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'commit_panel'  # deve corrispondere allo "slug" del tuo pannello
# The name of the dashboard the PANEL is associated with. Required.
PANEL_DASHBOARD = 'project'
# The name of the panel group the PANEL is associated with (opzionale se non usi gruppi).
PANEL_GROUP = 'default'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'custom_dashboard_plugin.panels.commit_panel.CommitPanel'
