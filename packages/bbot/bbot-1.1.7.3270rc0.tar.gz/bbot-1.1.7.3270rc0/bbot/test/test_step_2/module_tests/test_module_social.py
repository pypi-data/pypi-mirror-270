from .base import ModuleTestBase


class TestSocial(ModuleTestBase):
    targets = ["http://127.0.0.1:8888"]
    modules_overrides = ["httpx", "excavate", "social"]

    async def setup_after_prep(self, module_test):
        expect_args = {"method": "GET", "uri": "/"}
        respond_args = {
            "response_data": """
            <html>
                <a href="https://discord.gg/asdf"/><a href="https://github.com/blacklanternsecurity/bbot"/>
                <a href="https://hub.docker.com/r/blacklanternsecurity/bbot"/>
            </html>
            """
        }
        module_test.set_expect_requests(expect_args=expect_args, respond_args=respond_args)

    def check(self, module_test, events):
        assert any(
            e.type == "SOCIAL" and e.data["platform"] == "discord" and e.data["profile_name"] == "asdf" for e in events
        )
        assert any(
            e.type == "SOCIAL" and e.data["platform"] == "docker" and e.data["profile_name"] == "blacklanternsecurity"
            for e in events
        )
        assert any(
            e.type == "SOCIAL" and e.data["platform"] == "github" and e.data["profile_name"] == "blacklanternsecurity"
            for e in events
        )
