# Generated by Django 3.2.9 on 2021-11-26 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "dept_no",
                    models.CharField(
                        max_length=4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="code",
                    ),
                ),
                (
                    "dept_name",
                    models.CharField(max_length=40, unique=True, verbose_name="name"),
                ),
            ],
            options={
                "verbose_name": "department",
                "verbose_name_plural": "departments",
                "db_table": "departments",
                "ordering": ["dept_no"],
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "emp_no",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="employee number",
                    ),
                ),
                ("birth_date", models.DateField(verbose_name="birthday")),
                (
                    "first_name",
                    models.CharField(max_length=14, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=16, verbose_name="last name"),
                ),
                ("gender", models.CharField(max_length=1, verbose_name="gender")),
                ("hire_date", models.DateField(verbose_name="hire date")),
            ],
            options={
                "verbose_name": "employee",
                "verbose_name_plural": "employees",
                "db_table": "employees",
            },
        ),
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="title")),
                ("from_date", models.DateField(verbose_name="from")),
                ("to_date", models.DateField(blank=True, null=True, verbose_name="to")),
                (
                    "employee",
                    models.ForeignKey(
                        db_column="emp_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.employee",
                        verbose_name="employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "title",
                "verbose_name_plural": "titles",
                "db_table": "titles",
            },
        ),
        migrations.CreateModel(
            name="Salary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("salary", models.IntegerField(verbose_name="salary")),
                ("from_date", models.DateField(verbose_name="from")),
                ("to_date", models.DateField(verbose_name="to")),
                (
                    "employee",
                    models.ForeignKey(
                        db_column="emp_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.employee",
                        verbose_name="employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "salary",
                "verbose_name_plural": "salaries",
                "db_table": "salaries",
                "ordering": ["-from_date"],
            },
        ),
        migrations.CreateModel(
            name="DeptManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("from_date", models.DateField(verbose_name="from")),
                ("to_date", models.DateField(verbose_name="to")),
                (
                    "department",
                    models.ForeignKey(
                        db_column="dept_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.department",
                        verbose_name="department",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        db_column="emp_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.employee",
                        verbose_name="employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "department manager",
                "verbose_name_plural": "department managers",
                "db_table": "dept_manager",
                "ordering": ["-from_date"],
            },
        ),
        migrations.CreateModel(
            name="DeptEmp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("from_date", models.DateField(verbose_name="from")),
                ("to_date", models.DateField(verbose_name="to")),
                (
                    "department",
                    models.ForeignKey(
                        db_column="dept_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.department",
                        verbose_name="department",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        db_column="emp_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.employee",
                        verbose_name="employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "department employee",
                "verbose_name_plural": "department employees",
                "db_table": "dept_emp",
            },
        ),
    ]