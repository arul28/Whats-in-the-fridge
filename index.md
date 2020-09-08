## Honey! What's in the fridge?

What if there was an easier way to know what’s in your fridge?

The main focus of our project was to create a machine learning model with multi-label classification that could recognize everything in our fridge with just a picture. 

Obviously, this sort of idea is useless on its own, but the possible implementations could be hugely advantageous. Given just a weeks time, we just wanted to create the basis for such a project, which is the multi label classification. We trained chicken breasts, raw pork, milk, oranges, apples, bread, carrots, and broccoli.

![Image of fridge](images/fridge.jpg)

*Image of fridge with the 8 ingredients we wanted to train*

Below is our report in which we discuss how we trained and tested this model. In addition to this webpage, all the code we used will either be uploaded to the repository linked at the top or a link to that code will be mentioned at the bottom of this page.

### What Is Multi Label Classification?

To understand multi label classification, first we have to understand multi class classification as multi label is just an extension of multi label. Multi class classification is when you train a model to detect many different classes but only one at a time in the image. This is a categorical problem because it is only deciding which of the categories has the highest probability of being in the image. The output of a multi class classification model would only be one label. However, for multilabel classification, you train a model to detect many different classes but it can also detect many of them in the same image. It can assign many classification labels to one image. Multilabel classification is a binary problem because it is deciding, is this class in the picture, is the next one in the picture and so on. The number of outputs for multilabel classification is as many classes that you are training, in our case there are 8.

![multi-label classification image](images/multilabel.jpg)

*Visual representation of multi-label classification*

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/arul28/Whats-in-the-fridge/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
