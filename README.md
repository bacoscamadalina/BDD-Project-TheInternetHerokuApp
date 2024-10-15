# BDD Project The Internet-HerokuApp 🚀

## Project Structure 📂

| Directory/File     | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| **features/**      | 📄 Contains `.feature` files with test scenarios in Gherkin syntax.      |
| **steps/**         | 📝Python files with step definitions for the feature files.              |
| **pages/**         | 🏷️Page Object Model (POM) classes with web element selectors and methods. |
| **driver.py**      | 🌐Creates and configures the Selenium WebDriver.                         |
| **environment.py** | ⚙️Sets up and tears down tests (`before_all` and `after_all`).             |
| **behave.ini**     | 🛠️Configures Behave report formatters (e.g., HTML reports).                |

## Key Files 🔑

### `driver.py`
- 🌍 Initializes the Selenium WebDriver.

### `environment.py`
- **`before_all(context)`**: 🚦 Initializes the WebDriver and page objects.
- **`after_all(context)`**: ❌ Closes the WebDriver.

### `behave.ini`
- 📝 Configures Behave formatters, e.g., HTML reports.

## Running the Project ▶️

1. Clone the repository:
   ```bash
   % git clone https://github.com/bacoscamadalina/BDD-Project-TheInternetHerokuApp
   
2. Install the required dependencies
    ```
   % pip install -r requirements.txt

3. Run All Scenarios
    ```
   % behave

4. Generate HTML Raport
   ```
   % behave -f behave_html_formatter:HTMLFormatter -o behave-report.html

5.  Custom HTML Report
   ```
   % behave -f html -o report.html
   ```

## Notes 📌
- Page Objects: Located in pages/, abstract web elements and interactions.
- Step Definitions: Implemented in steps/, link to feature file steps.
 

