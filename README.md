# PITCH POOL
## An application that allows users to make pitches and get feedback on them. 9/9/2018


## By **[Jeff Musa](https://github.com/jeffmusa)**

## Description
[Pitch Pool](https://pitchtime.herokuapp.com/) is a web application that allows users to submit a pitch. Also, other users are allowed to vote on submitted pitches and leave comments to give their feedback on the pitches. For a user to submit a pitch, vote on a pitch or give feedback on a pitch they need to have an account. <br>

The pitches are organized by categories. Examples of categories: <br> 
- pickup lines
- interview pitches
- product pitches
- promotion pitches

## User Stories
As a user I would like:
* to view the different categories
* to see the pitches other people have posted
* to submit a pitch in any category
* to comment on the different pitches and leave feedback
* to vote on the pitch and give it a downvote or upvote

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : jon@doe.com <br> Username : jon101 <br> Password : doe1 | New user is registered |
| Log in | Your email : jon@doe.com <br> Password : doe1 | Logged in |
| Display pitch categories | Categories display on navbar | List of various pitch categories |
| See pitches from selected category | **Click** a category | Directed to a page with a list of pitches from the selected category |
| Create a pitch | **Click Add a pitch** | An authenticated user is directed to a page with a form where the user can create and submit a pitch |
| Comment on a pitch | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a pitch |

## Setup/Installation Requirements

* Click [Pitch Pool](https://pitchtime.herokuapp.com/) <br/>
  or <br/>
* Copy [Pitch Pool](https://pitchtime.herokuapp.com/) and  Paste the link on your prefered browerser

This requires internet connection.

## Known Bugs

- Vote count unavailable


## Technologies Used
- Python3.6
- Flask
- Bootstrap
- Postgres Database
- CSS
- HTML

### License

MIT (c) 2017 **[Jeff Musa](https://github.com/jeffmusa)**
