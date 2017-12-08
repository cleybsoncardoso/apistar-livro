from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls
from src import views


routes = [
    Route('/author', 'PUT', views.Author.store, name="create_author"),
    Route('/author', 'GET', views.Author.all, name="get_all_author"),
    Route('/author/{id}', 'GET', views.Author.get, name="get_author_by_id"),
    Route('/author/{id}', 'PATCH', views.Author.update, name="update_author"),
    Route('/author/{id}', 'DELETE', views.Author.delete, name="delete_author"),
    Route('/user', 'PUT', views.User.store, name="create_user"),    
    Route('/user', 'GET', views.User.all, name="get_all_users"),
    Route('/login', 'POST', views.User.login),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]