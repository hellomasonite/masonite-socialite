from masonite.managers import Manager


class SocialiteManager(Manager):
    config = 'socialite'
    driver_prefix = 'Socialite'

    def driver(self, driver):
        if '-' in driver:
            driver = driver.split('-')[0]
        return super().driver(driver)
