# Website for Students' Club

Hello, I am a board member of the students' club known as "Young Entrepreneurs' Club" (Genç Girişimciler Kulübü in Turkish) and also a Sophomore Computer Science student. 
While spending time within this club I came to realize that the club lacked a proper website, so I decided to create one from stratch.


## Development

I used Django combined with Bootstrap to create the website. Even though this project has been virtually completed, I still need to develop some parts of it.
Especially since I decided to completely change the design mid-development because of the feedback I got.


## Demo

After the development phase is over, we will need to contact the school administration in order to receive funding and permissions to deploy the website.
So, in order to show what the website actually looks like, I am including a link to a video in which I locally host the website for demo purposes.


https://drive.google.com/drive/folders/1GN0vfa6lt_wTBiQp8hMswGLD3mfkZ27q?usp=sharing


## Features

The website is intended to be used for long term. Since not everyon in the upcoming generations of the club will be Computer Science majors, 
I intended the website to be completely manageable by someone with no programing knowledge.

Thus, the website will automatically regulate itself with changed made by the superuser. 
When a new event is added to the website, it will automatically create an appropriate page for it. 
Address of the place the club event is going to take place will be automatically added to places where it is appropriate.

If the event has its very own website, the "learn more about this event" link will redirect there. If not, the website will automatically create one.
If the event requires to buy tickets from an outside source, that will be linked too and "join this event" page will prompt the user that this event requires buying tickets.
If not, it will display a message that means showing up for the event is enough for participation.

If even has sponsors, it will automatically generate a sponsors page for it and automatically edit it. If the sponsor has a website, clicking on their logo will result in a redirection.
On top of that, sponsorship categories that do not have any sponsors will not be displayed at all (if there are monetary sponsors and no food sponsors, the "food sponsors" category will be completely hidden to avoid an awkward title with no logos)
Having said that, same treatment is done for participants and/or speakers too, just with a different design.

Headers of events will also be dynamically edited. For example, if the even does not have any sponsors at all, "sponsorships" link will be completely removed.

When someone attempts to contact the club via the website, the website will automatically create and format an email and send it to the email address of the club.

Another feature of this website that I am very exicted about is blog. Blog allows to for registration of multiple users so that our members can add articles to blog.
But since that feature can be used for bad intentions, I also implemented a "check" feature. When the user adds an article to the blog, the article has to be checked by the superuser to be deployed to the site.

Blog will probably be used for announcing upcoming events so when there is an upcoming event, the first page of the blog will automatically change to promote the event and will display the default design when there's no upcoming events.

Blog page also contains a twitter widget that shows tweets by our Twitter account.
