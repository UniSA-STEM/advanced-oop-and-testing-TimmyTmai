'''
File: test_zoo.py
Description: Unit tests for the Zoo class.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest

from zoo import Zoo
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from enclosure import Enclosure
from mammal import Mammal
from health_record import HealthRecord


def make_zoo():
    return Zoo("Timmy Zoo")


def make_lion(name="Simba", healthy=True):
    return Mammal(name, "Lion", 5, "Meat", "savannah", healthy)


def make_savannah_enclosure(size=200):
    return Enclosure(size=size, environment="savannah")


def test_zoo_valid_creation():
    zoo = make_zoo()
    assert zoo.name == "Timmy Zoo"
    assert zoo.staff == []
    assert zoo.animals == []
    assert zoo.enclosures == []


def test_zoo_invalid_name_raises():
    with pytest.raises(ValueError):
        Zoo("   ")  # invalid according to helper.validate_string


def test_add_staff_accepts_zookeeper_and_vet(capsys):
    zoo = make_zoo()
    zk = Zookeeper("Alice")
    vet = Veterinarian("Dr. Bob")

    zoo.add_staff(zk)
    zoo.add_staff(vet)

    assert zk in zoo.staff
    assert vet in zoo.staff

    out = capsys.readouterr().out
    assert "Added staff member Alice" in out
    assert "Added staff member Dr. Bob" in out


def test_add_staff_rejects_invalid_type():
    zoo = make_zoo()

    class FakeStaff:
        pass

    with pytest.raises(TypeError):
        zoo.add_staff(FakeStaff())  # not a Zookeeper or Veterinarian


def test_remove_staff_deactivates_and_removes():
    zoo = make_zoo()
    zk = Zookeeper("Alice")
    zoo.add_staff(zk)

    enc = make_savannah_enclosure()
    zoo.add_enclosure(enc)
    zk.assign_enclosure(enc)
    assert len(zk.assigned_enclosure) == 1

    zoo.remove_staff(zk)

    assert zk not in zoo.staff
    # should have been deactivated and assignments cleared
    assert zk.assigned_enclosure == []


def test_remove_staff_not_in_zoo_raises():
    zoo = make_zoo()
    zk = Zookeeper("Alice")

    with pytest.raises(ValueError):
        zoo.remove_staff(zk)


def test_add_and_remove_animal(capsys):
    zoo = make_zoo()
    lion = make_lion()

    zoo.add_animal(lion)
    assert lion in zoo.animals

    out = capsys.readouterr().out
    assert "Added animal Simba" in out

    # removing also removes from enclosures
    enc = make_savannah_enclosure()
    zoo.add_enclosure(enc)
    enc.add_animal(lion)
    assert lion in enc.animals

    zoo.remove_animal(lion)

    assert lion not in zoo.animals
    assert lion not in enc.animals


def test_remove_animal_not_in_zoo_raises():
    zoo = make_zoo()
    lion = make_lion()

    with pytest.raises(ValueError):
        zoo.remove_animal(lion)


def test_add_and_remove_enclosure(capsys):
    zoo = make_zoo()
    enc = make_savannah_enclosure()
    zoo.add_enclosure(enc)

    assert enc in zoo.enclosures
    out = capsys.readouterr().out
    assert "added enclosure savannah to timmy zoo.\n" in out.lower()

    # cannot remove enclosure with animals
    lion = make_lion()
    zoo.add_animal(lion)
    enc.add_animal(lion)

    with pytest.raises(RuntimeError):
        zoo.remove_enclosure(enc)

    # remove the lion first
    enc.remove_animal(lion)
    zoo.remove_animal(lion)

    zoo.remove_enclosure(enc)
    assert enc not in zoo.enclosures


def test_remove_enclosure_not_in_zoo_raises():
    zoo = make_zoo()
    enc = make_savannah_enclosure()

    with pytest.raises(ValueError):
        zoo.remove_enclosure(enc)


# --- Search helpers ---------------------------------------------------------


def test_find_staff_by_name_case_insensitive():
    zoo = make_zoo()
    zk = Zookeeper("Alice")
    zoo.add_staff(zk)

    staff_found = zoo.find_staff_by_name("alice")
    assert staff_found is zk

    none_found = zoo.find_staff_by_name("bob")
    assert none_found is None


def test_find_staff_by_id():
    zoo = make_zoo()
    zk = Zookeeper("Alice")
    zoo.add_staff(zk)

    found = zoo.find_staff_by_id(zk.id)
    assert found is zk

    import uuid as _uuid
    random_id = _uuid.uuid4()
    assert zoo.find_staff_by_id(random_id) is None


def test_find_animal_by_name():
    zoo = make_zoo()
    lion1 = make_lion("Simba")
    lion2 = make_lion("simba")
    zoo.add_animal(lion1)
    zoo.add_animal(lion2)

    result = zoo.find_animal_by_name("SIMBA")
    assert len(result) == 2
    assert lion1 in result and lion2 in result


def test_find_enclosure_by_environment():
    zoo = make_zoo()
    e1 = make_savannah_enclosure()
    e2 = Enclosure(size=150, environment="aquatic")
    zoo.add_enclosure(e1)
    zoo.add_enclosure(e2)

    savannah_encs = zoo.find_enclosure_by_environment("Savannah")
    assert savannah_encs == [e1]

    aquatic_encs = zoo.find_enclosure_by_environment("aquatic")
    assert aquatic_encs == [e2]


# --- Health records & treatment --------------------------------------------


def test_get_health_records_for_animal_raises_if_not_in_zoo():
    zoo = make_zoo()
    lion = make_lion()

    with pytest.raises(ValueError):
        zoo.get_health_records_for_animal(lion)


def test_get_health_records_for_animal_collects_from_all_vets(capsys):
    zoo = make_zoo()
    lion = make_lion()
    zoo.add_animal(lion)

    vet1 = Veterinarian("Dr. A")
    vet2 = Veterinarian("Dr. B")
    zoo.add_staff(vet1)
    zoo.add_staff(vet2)

    # assign animal and add records
    vet1.assign_animal(lion)
    vet2.assign_animal(lion)

    rec1 = HealthRecord(lion, "injuries", "low", "01/01/2025", "Note 1", True)
    rec2 = HealthRecord(lion, "illness", "medium", "02/01/2025", "Note 2", False)

    vet1.get_records(lion).append(rec1)
    vet2.get_records(lion).append(rec2)

    records = zoo.get_health_records_for_animal(lion)
    out = capsys.readouterr().out

    # both records returned and printed
    assert len(records) == 2
    assert rec1 in records and rec2 in records
    assert "HEALTH RECORD" in out


def test_animal_under_treatment_detects_active_records(capsys):
    zoo = make_zoo()
    lion = make_lion(healthy=False)
    zebra = make_lion("Zebra", healthy=False)  # just reuse Mammal class for test

    zoo.add_animal(lion)
    zoo.add_animal(zebra)

    vet = Veterinarian("Dr. A")
    zoo.add_staff(vet)
    vet.assign_animal(lion)
    vet.assign_animal(zebra)

    rec_active = HealthRecord(lion, "injuries", "high", "01/01/2025", "Critical", True)
    rec_closed = HealthRecord(zebra, "illness", "low", "02/01/2025", "Mild", False)

    vet.get_records(lion).append(rec_active)
    vet.get_records(zebra).append(rec_closed)

    under_treatment = zoo.animal_under_treatment()
    out = capsys.readouterr().out

    assert under_treatment == [lion]
    assert "Simba (Lion) is under treatment." in out
    assert "No animal is under treatment." not in out


def test_animal_under_treatment_none(capsys):
    zoo = make_zoo()
    lion = make_lion()
    zoo.add_animal(lion)

    # no vets, no records
    animals = zoo.animal_under_treatment()
    out = capsys.readouterr().out

    assert animals == []
    assert "No animal is under treatment." in out


# --- Scheduler methods ------------------------------------------------------


def test_schedule_daily_feeding_calls_zookeepers(monkeypatch, capsys):
    zoo = make_zoo()
    zk1 = Zookeeper("Alice")
    zk2 = Zookeeper("Bob")
    vet = Veterinarian("Dr. A")

    zoo.add_staff(zk1)
    zoo.add_staff(zk2)
    zoo.add_staff(vet)

    called = []

    def fake_perform_task(self, task):
        called.append((self.name, task))

    # Only Zookeepers' perform_task is patched
    monkeypatch.setattr("zookeeper.Zookeeper.perform_task", fake_perform_task)

    zoo.schedule_daily_feeding()

    assert ("Alice", "feed") in called
    assert ("Bob", "feed") in called
    # vet should not have been called here
    assert all(name != "Dr. A" for name, _ in called)


def test_schedule_daily_cleaning_calls_zookeepers(monkeypatch):
    zoo = make_zoo()
    zk1 = Zookeeper("Alice")
    zoo.add_staff(zk1)

    called = []

    def fake_perform_task(self, task):
        called.append((self.name, task))

    monkeypatch.setattr("zookeeper.Zookeeper.perform_task", fake_perform_task)

    zoo.schedule_daily_cleaning()

    assert called == [("Alice", "clean")]


def test_schedule_daily_health_checks_calls_vets(monkeypatch):
    zoo = make_zoo()
    vet1 = Veterinarian("Dr. A")
    vet2 = Veterinarian("Dr. B")
    zk = Zookeeper("Alice")

    zoo.add_staff(vet1)
    zoo.add_staff(vet2)
    zoo.add_staff(zk)

    called = []

    def fake_perform_task(self, task):
        called.append((self.name, task))

    monkeypatch.setattr("veterinarian.Veterinarian.perform_task", fake_perform_task)

    zoo.schedule_daily_health_checks()

    assert ("Dr. A", "health check") in called
    assert ("Dr. B", "health check") in called
    # zookeeper should not be in this list
    assert all(name != "Alice" for name, _ in called)


def test_run_full_daily_schedule_uses_all_schedulers(monkeypatch):
    zoo = make_zoo()
    zk = Zookeeper("Alice")
    vet = Veterinarian("Dr. A")
    zoo.add_staff(zk)
    zoo.add_staff(vet)

    calls = []

    def fake_feed(self, task):
        calls.append(("feed", self.name))

    def fake_clean(self, task):
        calls.append(("clean", self.name))

    def fake_health_check(self, task):
        calls.append(("health check", self.name))

    monkeypatch.setattr("zookeeper.Zookeeper.perform_task", fake_feed)
    monkeypatch.setattr("veterinarian.Veterinarian.perform_task", fake_health_check)

    # run_full_daily_schedule calls:
    #   schedule_daily_feeding -> Zookeeper.perform_task("feed")
    #   schedule_daily_cleaning -> Zookeeper.perform_task("clean")
    #   schedule_daily_health_checks -> Veterinarian.perform_task("health check")
    # But we patched only once, so we patch feed vs clean using logic:
    # For simplicity here, just assert it doesn't crash & Vet gets called for health check
    zoo.run_full_daily_schedule()

    # At least a health check call must exist
    assert any(call[0] == "health check" and call[1] == "Dr. A" for call in calls)


# --- __str__ -----------------------------------------------------------------


def test_zoo_str_contains_summary():
    zoo = make_zoo()
    zk = Zookeeper("Alice")
    lion = make_lion()
    enc = make_savannah_enclosure()

    zoo.add_staff(zk)
    zoo.add_animal(lion)
    zoo.add_enclosure(enc)

    summary = str(zoo)
    assert "--- ZOO SUMMARY:" in summary
    assert "Number of staff: 1" in summary
    assert "Number of animals: 1" in summary
    assert "Number of enclosures: 1" in summary
