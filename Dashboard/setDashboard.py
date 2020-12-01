import json

with open("count.json", "r") as read_file:
    data = json.load(read_file)

print(data)

up = data['up']
left = data['left']
down = data['down']
right = data['right']
select = data['select']

print(up, left, down, right, select)

f = open('Dashboard/dashboard_graph.html', 'w')

html_content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <!-- viewport meta -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="MartPlace - Complete Online Multipurpose Marketplace HTML Template">
    <meta name="keywords" content="app, app landing, product landing, digital, material, html5">


    <title>Martplace - Dashboard setting</title>

    <!-- inject:css -->
    <link rel="stylesheet" href="css/animate.css">
    <link rel="stylesheet" href="css/font-awesome.min.css">
    <link rel="stylesheet" href="css/fontello.css">
    <link rel="stylesheet" href="css/jquery-ui.css">
    <link rel="stylesheet" href="css/lnr-icon.css">
    <link rel="stylesheet" href="css/owl.carousel.css">
    <link rel="stylesheet" href="css/slick.css">
    <link rel="stylesheet" href="css/trumbowyg.min.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <!-- endinject -->

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="16x16" href="images/favicon.png">
</head>

<body class="preload dashboard-setting">
    <!--================================
        START BREADCRUMB AREA
    =================================-->
    <section class="breadcrumb-area">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h1 class="page-title">Dashboard</h1>
                </div>
                <!-- end /.col-md-12 -->
            </div>
            <!-- end /.row -->
        </div>
        <!-- end /.container -->
    </section>
    <!--================================
        END BREADCRUMB AREA
    =================================-->

    <!--================================
            START DASHBOARD AREA
    =================================-->
    <section class="dashboard-area">
        <div class="dashboard_menu_area">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <ul class="dashboard_menu">
                            <li class="active">
                                <a href="dashboard_about.html">
                                    <span class="lnr lnr-home"></span>About</a>
                            </li>
                            <li>
                                <a href="dashboard_graph.html">
                                    <span class="lnr lnr-cog"></span>Graph</a>
                            </li>
                        </ul>
                        <!-- end /.dashboard_menu -->
                    </div>
                    <!-- end /.col-md-12 -->
                </div>
                <!-- end /.row -->
            </div>
            <!-- end /.container -->
        </div>
        <!-- end /.dashboard_menu_area -->
    </section>
    <!--================================
            END DASHBOARD AREA
    =================================-->

    <!--============================================
        START SINGLE PRODUCT DESCRIPTION AREA
    ==============================================-->
    <section class="single-product-desc single-product-desc2">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="dashboard_title_area">
                        <div class="dashboard__title">
                            <h3>Quantidade de sinais</h3>
                        </div>
                    </div>
                </div>
                <!-- end /.col-md-12 -->
            </div>
                <!-- end /.row -->
            <div class="row">
                <div class="col-lg-8">
                    <div class="item-preview item-preview2">
                        <div class="prev-slide">
                            <img src="img/graph.png" alt="Erro ao ler grafico.">
                        </div>

                        <div class="item__preview-thumb">
                            <ul class= 'data'>
                                <li>
                                    <p>
                                        <span class ='lnr lnr-question ' style="border-radius: 50%; background-color: #fff032; color: #fff032; height: 1000px; width: 1000px;", > ... </span>
                                    Mover para cima</p>
                                </li>
                                <li>
                                    <p>
                                        <span class ='lnr lnr-question ' style="border-radius: 50%; background-color: #003153; color: #003153; height: 1000px; width: 1000px;", > ... </span>
                                    Mover para esquerda</p>
                                </li>
                                <li>
                                    <p>
                                        <span class ='lnr lnr-question ' style="border-radius: 50%; background-color: #1ee63c; height: 1000px; color: #1ee63c; width: 1000px;", > ... </span>
                                    Mover para baixo</p>
                                </li>
                                <li>
                                    <p>
                                        <span class ='lnr lnr-question ' style="border-radius: 50%; background-color: #fa1e28; height: 1000px; color: #fa1e28; width: 1000px;", > ... </span>
                                    Mover para direita</p>
                                </li>
                                <li>
                                    <p>
                                        <span class ='lnr lnr-question ' style="border-radius: 50%; background-color: #fc0fc0; height: 1000px; color: #fc0fc0; width: 1000px;", > ... </span>
                                    Selecionar</p>
                                </li>

                            </ul>
                        </div>
                    </div>
                    <!-- end /.item-preview-->
                </div>
                <!-- end /.col-md-8 -->

                <div class="col-lg-4">
                    <aside class="sidebar sidebar--single-product">
                        <div class="sidebar-card card--metadata">
                            <ul class="data">
                                <li>
                                    <p>
                                        <span"></span>Mover para cima</p>
                                    <span id= "up">{up}</span>
                                </li>
                                <li>
                                    <p>
                                        <span"></span>Mover para esquerda</p>
                                    <span id="left">{left}</span>
                                </li>
                                <li>
                                    <p>
                                        <span"></span>Mover para baixo</p>
                                    <span id= "down">{down}</span>
                                </li>
                                <li>
                                    <p>
                                        <span"></span>Mover para direita</p>
                                    <span id= "right">{right}</span>
                                </li>
                                <li>
                                    <p>
                                        <span"></span>Selecionar</p>
                                    <span id= "select">{select}</span>
                                </li>
                            </ul>
                        </div>
                        <!-- end /.sidebar-card -->
                        <!-- end /.aside -->
                    </aside>
                    <!-- end /.aside -->
                </div>
                <!-- end /.col-md-4 -->
            </div>
            <!-- end /.row -->
        </div>
        <!-- end /.container -->
    </section>
    <!--===========================================
        END SINGLE PRODUCT DESCRIPTION AREA
    ===============================================-->

    <!--//////////////////// JS GOES HERE ////////////////-->
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyA0C5etf1GVmL_ldVAichWwFFVcDfa1y_c"></script>
    <!-- inject:js -->
    <script src="js/jquery-1.12.3.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/uikit.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/chart.bundle.min.js"></script>
    <script src="js/grid.min.js"></script>
    <script src="js/jquery-ui.min.js"></script>
    <script src="js/jquery.barrating.min.js"></script>
    <script src="js/jquery.countdown.min.js"></script>
    <script src="js/jquery.counterup.min.js"></script>
    <script src="js/jquery.easing1.3.js"></script>
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/slick.min.js"></script>
    <script src="js/tether.min.js"></script>
    <script src="js/trumbowyg.min.js"></script>
    <script src="js/waypoints.min.js"></script>
    <script src="js/dashboard.js"></script>
    <script src="js/main.js"></script>
    <script src="js/map.js"></script>

    <!-- endinject -->
</body>

</html>
"""

f.write(html_content)
f.close()
