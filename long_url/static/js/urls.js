function longurl_controller($scope, $http) {
    $scope.ident = "";
    $scope.url = 'expnd.me';

    $scope.get_ident = function() {
        $http.get('../create/?to=' + $scope.url).
            success(function(data) {
                $scope.ident = 'http://expnd.me/forward/' + data.ident;
                //$scope.ident = data.ident;
            });
        return undefined;
    }

    $scope.copy = function copyToClipboard() {
      window.prompt("Copy to clipboard: Ctrl+C, Enter", $scope.ident);
    }
}