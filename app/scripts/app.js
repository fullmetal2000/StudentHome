'use strict';

angular
  .module('sth', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute',
    'sth.home',
    'sth.login',
    'ui.bootstrap'

  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
//   .controller('MainCtrl',['$scope','$rootScope','$http',function($scope, $rootScope, $http){
//     console.log('this is app.js')

// var TabsDemoCtrl = function ($scope) {
//   $scope.tabs = [
//     { title:"Dynamic Title 1", content:"Dynamic content 1" },
//     { title:"Dynamic Title 2", content:"Dynamic content 2", disabled: true }
//   ];

//   $scope.alertMe = function() {
//     setTimeout(function() {
//       alert("You've selected the alert tab!");
//     });
//   };

//   $scope.navType = 'pills';

//   }])
