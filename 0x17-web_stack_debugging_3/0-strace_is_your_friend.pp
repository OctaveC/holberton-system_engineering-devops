# Fixing error 500

exec {'replace':
command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
path    => '/usr/local/bin/:/bin/'
}
