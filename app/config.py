class DevelopmentConfig():
    DEBUG=True
    #Configuracion base de datos
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD = ''
    MYSQL_DB='api_personajes'

config={
    'development':DevelopmentConfig
}