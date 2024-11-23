import requests

# Replace with your GitHub username
username = 'rebeccadsouza04'

# GitHub API URL to get the repository details
url = f'https://api.github.com/users/{username}/repos?per_page=100'

# Send a GET request to fetch the repositories
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    repos = response.json()

    # Prepare the Markdown table header
    markdown_table = '''## 📂 My GitHub Repositories

| Repository Name        | Stars | Forks | Open Issues | Pull Requests | Technology Stack            |
|------------------------|-------|-------|-------------|---------------|-----------------------------|
'''

    # Loop through repositories to fetch the required details
    for repo in repos:
        repo_name = repo['name']
        stars = repo['stargazers_count']
        forks = repo['forks_count']
        open_issues = repo['open_issues_count']
        # Pull request count is not directly available, so we can leave it or use another method
        pull_requests = 'TBD'  # Placeholder as GitHub doesn't provide an API endpoint to get pull requests count
        tech_stack = 'TBD'  # Placeholder for tech stack; you can manually add or use another method

        # Add the repository info to the table
        markdown_table += f'| [{repo_name}](https://github.com/{username}/{repo_name}) | {stars} | {forks} | {open_issues} | {pull_requests} | {tech_stack} |\n'

    # Write the table to your README.md file
    with open('README.md', 'a') as f:
        f.write(markdown_table)
    
    print("README.md file has been updated with the repository stats!")

else:
    print(f"Failed to fetch repositories: {response.status_code}")
