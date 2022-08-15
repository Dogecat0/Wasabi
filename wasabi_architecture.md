# **Collecting recipe data**

### - **Scraping recipe data using API on all possible websites.**

<ol type="1">
    <li>Using 'recipe-scrapers' to get the recipe data from websites listed by it.</li>
    <ol type="a">
        <li>Crawl the whole website and filter out the non-recipe parts using something like 'Food52.schema.data' filled out by 'extruct'. </li>
    </ol>
</ol>

### - **Build a database for hosting recipe data.**

<ol type="1">
    <li>Store everything from schema data above.</li>
    <li>Create timestamp of each crawl of recipe data.</li>
</ol>

### - **Clean the scraped content and transform them into a proper dataset.**

<ol type="1">
    <li>Design the dataset schema</li>
    <ol type="a">
        <li>recipe title</li>
        <li>cooking time</li>
        <li>ingredients</li>
        <li>difficulty</li>
        <li>instructions (e.g. the number of steps)</li>
        <li>user name</li>
        <li>date of birth</li>
        <li>password</li>
        <li>email address</li>
        <li>user location</li>
        <li>dietary preference</li>
        <li>database indexes for fast lookups (e.g. different cuisines, alcohol included)</li>
        <li>supermarkets info (e.g. opening time, location, prices for ingredients by cities, item availability)</li>
    </ol>
</ol>

---

# **Create the best recipe for recommendations**

### - **Step 1: Get and rank recipes.**

<ol type="1">
    <li>Using regression model to predict the rankings of each recipe (e.g. a continuous rating number from 0 to 1 which should be scaled from 0 to 5 stars).</li>
    <li>Using NLP sentiment model to perform the sentiment analysis of all the comments for each recipe.</li>
    <ol type="a">
        <li>Get all the comments data from each recipe.</li>
        <li>Perform sentiment analysis and get a score for each comment.</li>
        <li>Average the sentiment scores for all comments and get the final sentiment score for each recipe.</li>
    </ol>    
</ol>

### - **Step 2: Introduce generic filtering systems to help users to get the ideal recipes.**

<ol type="1">
    <li>Floating number toggle filter (e.g. number of comments, ratings, calories or nutrition information).</li>
    <li>Class filter (e.g. veg/vegan/non, gluten free/not free).</li>
</ol>

---

# **Find the best price match on supermarkets' websites of all ingredients (Future feature)**
### - **Scraping the supermarkets' websites to get the real time price for each item listed in the recommended recipes.**