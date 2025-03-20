=======================================
Contributing to Darca Exception
=======================================

Thank you for considering contributing to **Darca Exception**!  
Contributions help make this project better, and we welcome **bug reports, feature requests, and pull requests**.  

---

🚀 **How to Contribute**
--------------------
We welcome contributions in the following ways:

- **Report Bugs** – If you find an issue, please report it under `Issues`.
- **Request Features** – Have a great idea? Open a feature request!
- **Submit Pull Requests** – Help improve the project by fixing bugs or adding enhancements.

---

🔍 **Reporting Bugs**
--------------------
If you find a bug, please check the `Issues` tab to see if it has already been reported.  
If not, create a new issue with the following details:

1. **Describe the bug** – What is happening?
2. **Steps to reproduce** – How can we reproduce the bug?
3. **Expected behavior** – What should happen instead?
4. **Screenshots or logs (if applicable)** – Helps us understand the issue better.
5. **Environment details** – Python version, OS, etc.

📌 **Submit your bug report here:**  
`https://github.com/roelkist/darca-exception/issues`

---

💡 **Requesting Features**
--------------------
Have an idea to improve the project? Submit a **Feature Request** with:

1. **Feature description** – Explain your idea clearly.
2. **Use case** – How would this help users?
3. **Potential implementation** (if possible) – Any thoughts on how to add it?

📌 **Submit your feature request here:**  
`https://github.com/roelkist/darca-exception/issues`

---

🛠 **Submitting a Pull Request (PR)**
--------------------
### **1. Fork & Clone**
First, clone the repository:

.. code-block:: bash

    git clone https://github.com/roelkist/darca-exception.git
    cd darca-exception

### **2. Create a New Branch**
Always create a new branch for your contribution:

.. code-block:: bash

    git checkout -b feature/new-exception-handler

### **3. Install Dependencies**
Set up your environment:

.. code-block:: bash

    make install

### **4. Make Your Changes**
- Follow the project’s coding style.
- Ensure your code is **well-documented** and **tested**.

### **5. Run Pre-Commit & Tests**
Before submitting, ensure everything is correctly formatted and tested:

.. code-block:: bash

    make check  # Formats, runs pre-commit, and tests

### **6. Commit and Push**
Commit your changes with a meaningful message:

.. code-block:: bash

    git add .
    git commit -m "Add new exception type for better error handling"
    git push origin feature/new-exception-handler

### **7. Open a Pull Request**
- Go to the repository on GitHub.
- Click "New Pull Request".
- Select your branch and submit the PR.

**PR Guidelines:**
- **Reference the related issue (if applicable).**
- **Explain what your PR does and why it's needed.**
- **Include test results/screenshots if relevant.**

---

✅ **Code Guidelines**
--------------------
To maintain code consistency, follow these guidelines:

1. **Formatting** – Code should be formatted using `black` and `isort`:
   
   .. code-block:: bash

       make format

2. **Linting & Static Analysis** – Run `pre-commit` before pushing:

   .. code-block:: bash

       make precommit

3. **Testing** – Ensure all tests pass:

   .. code-block:: bash

       make test

4. **Keep Changes Focused** – PRs should be **small and focused** on one feature or bug fix.

---

📖 **Documentation Contributions**
--------------------
If you're improving documentation:

- Edit the RST files in `docs/source/`.
- Run:

  .. code-block:: bash

      make docs

- Open a PR with your improvements!

---

🗑 **Cleaning Up**
--------------------
To remove virtual environments and reset dependencies:

.. code-block:: bash

    make clean

---

🎉 **Thank You!**
--------------------
Your contributions make **Darca Exception** better for everyone! 🚀  
Feel free to ask questions or discuss improvements in the **Issues** section.

---
