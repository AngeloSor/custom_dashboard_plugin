# devstack/plugin.sh - DevStack plugin per custom_dashboard_plugin

function install_custom_dashboard_plugin {
    echo_summary "Installing Custom Dashboard Plugin"
    # Se Horizon è abilitato, copia (o crea un symlink) il file di registrazione nella cartella enabled di Horizon
    if is_service_enabled horizon; then
        # $DEST rappresenta la directory base di DevStack (solitamente /opt/stack)
        cp -a $DEST/custom_dashboard_plugin/enabled/_20_commit_panel.py $DEST/horizon/openstack_dashboard/enabled/_20_commit_panel.py
    fi
}

function configure_custom_dashboard_plugin {
    echo_summary "Configuring Custom Dashboard Plugin"
    # Se necessario per altre eventuali configurazioni
    :
}

if is_service_enabled horizon; then
    echo_summary "Custom Dashboard Plugin: Installing"
    install_custom_dashboard_plugin
    configure_custom_dashboard_plugin
fi
