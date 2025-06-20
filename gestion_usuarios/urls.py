from django.urls import path
from .views import (
    UsuarioList,
    UsuarioCreate,
    UsuarioUpdate,
    UsuarioDelete,
    acciones_backup,  
    exportar_usuarios_sql,
    importar_usuarios_sql,
    guardar_config_backup,
    descargar_backup,
    visualizar_backup,
    cambiar_rol_usuario,  
    register_user,
    login_user,
    logout_user,
    recuperar_password,
    buzon_notificaciones,
    contacto,
)

urlpatterns = [
    path('', UsuarioList.as_view(), name='usuario_lista'),
    path('nuevo/', UsuarioCreate.as_view(), name='usuario_nuevo'),
    path('editar/<int:pk>/', UsuarioUpdate.as_view(), name='usuario_editar'),
    path('eliminar/<int:pk>/', UsuarioDelete.as_view(), name='usuario_eliminar'),
    path('rol/<int:pk>/', cambiar_rol_usuario, name='cambiar_rol_usuario'),
    
    path('logout/', logout_user, name='logout_user'),
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('recuperar/', recuperar_password, name='recuperar_password'),
    path('buzon/', buzon_notificaciones, name='buzon'),
    path('contacto/', contacto, name='contacto'),


    #backups
    path('acciones/', acciones_backup, name='acciones_backup'),
    path('acciones/exportar/', exportar_usuarios_sql, name='exportar_usuarios_sql'),
    path('acciones/importar/', importar_usuarios_sql, name='importar_usuarios_sql'),
    path('acciones/configurar/', guardar_config_backup, name='config_backup_guardar'),
    path('backup/descargar/<str:archivo_nombre>/', descargar_backup, name='descargar_backup'),
    path('backup/visualizar/<str:archivo_nombre>/', visualizar_backup, name='visualizar_backup'),

]
