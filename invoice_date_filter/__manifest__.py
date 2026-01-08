{
    'name': 'Filtro de Rango de Fechas en Facturas',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Agrega búsqueda por fecha inicio y fin en facturas',
    'description': """
        Este módulo agrega dos opciones en la barra de búsqueda de facturas:
        - Fecha Inicio (Desde)
        - Fecha Fin (Hasta)
        Permite filtrar facturas por un rango específico escribiendo la fecha.
    """,
    'author': 'Ernesto Prevost',
    'depends': ['account'],
    'data': [
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}