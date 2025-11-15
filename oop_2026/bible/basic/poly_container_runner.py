
import redis
import requests


class ContainerRunner:
    def __init__(self, image, timeout=30):
        self.image = image
        self.timeout = timeout

    def deploy(self):
        container_id = self.start_container()
        if self._wait_for_health():
            return container_id
        self.stop_container(container_id)
        raise RuntimeError("Health check failed")

    def _wait_for_health(self):
        # Common retry logic
        for _ in range(self.timeout):
            if self.health_check():
                return True
            time.sleep(1)
        return False

    def start_container(self):
        return f"docker run -d {self.image}"

    def health_check(self):
        return True  # Base implementation


class WebAppRunner(ContainerRunner):
    def health_check(self):
        return requests.get(f"http://localhost/health").ok


class DatabaseRunner(ContainerRunner):
    def health_check(self):
        return psycopg2.connect(host="localhost").closed == False


class RedisRunner(ContainerRunner):
    def __init__(self, image, host="localhost", port=6379, timeout=30):
        super().__init__(image, timeout)
        self.host = host
        self.port = port

    def health_check(self):
        try:
            r = redis.Redis(host=self.host, port=self.port, socket_connect_timeout=1)
            return r.ping()
        except (redis.ConnectionError, redis.TimeoutError):
            return False


class FlaskAppRunner(ContainerRunner):
    def __init__(self, image, host="localhost", port=5000, timeout=30):
        super().__init__(image, timeout)
        self.host = host
        self.port = port

    def health_check(self):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/health", timeout=1)
            return response.status_code == 200
        except requests.RequestException:
            return False