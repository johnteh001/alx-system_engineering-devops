# fixing apache 500 error
exec { 'fix err':
onlyif  => 'test -e /var/www/html/wp-settings.php',
command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
path    => '/usr/local/sbin/:/usr/local/bin:/usr/sbin/:/usr/bin:/sbin/:/bin'
}
