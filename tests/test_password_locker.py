import pytest
from oop_2026.bible.basic.poly_interface import PasswordLocker


@pytest.fixture
def locker(tmp_path):
    """Provides a fresh PasswordLocker with a temp file path."""
    pl = PasswordLocker("secret123")
    pl.filepath = tmp_path / "password.txt"   # assuming save/load use this
    return pl


def test_lock_returns_true(locker):
    """Locking should return True and prevent access."""
    assert locker.lock() is True


def test_unlock_returns_true(locker):
    """Unlocking should return True when already locked."""
    locker.lock()
    assert locker.unlock() is True


def test_show_password_when_unlocked(locker):
    """Password should be shown when unlocked."""
    locker.unlock()
    assert locker.show_password() == "secret123"


def test_show_password_when_locked_raises(locker):
    """show_password should fail when locked."""
    locker.lock()
    with pytest.raises(Exception):
        locker.show_password()


def test_save_creates_file(locker):
    """Saving should create a file containing the password."""
    locker.save()
    assert locker.filepath.exists()
    assert locker.filepath.read_text() == "secret123"


def test_load_restores_password(locker):
    """Loading should restore password from file."""
    # manually write file first
    locker.filepath.write_text("restored_pw")
    locker.load()
    assert locker.show_password() == "restored_pw"
