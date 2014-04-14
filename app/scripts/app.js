'use strict';

angular
  .module('sth', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ui.router',
    'sth.home',
    'sth.login',
    'ui.bootstrap'

  ]).config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
 // For any unmatched url, send to /route1
      
      $stateProvider
        .state('login',{
          url:"/login",
          templateUrl:"views/login.html"
        })
        .state('page1', {
            url: "/page1",
            templateUrl: "views/page1.html"
        })
          .state('page1.list', {
              url: "/list",
              templateUrl: "route1.list.html",
              controller: function($scope){
                $scope.items = ["A", "List", "Of", "Items"];
              }
          })
          
        .state('page2', {
            url: "/page2",
            templateUrl: "views/page2.html"
        })
          .state('page2.list', {
              url: "/list",
              templateUrl: "route2.list.html",
              controller: function($scope){
                $scope.things = ["A", "Set", "Of", "Things"];
              }
          })
        $urlRouterProvider.otherwise('/');
    }])
