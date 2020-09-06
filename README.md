# NOTES

## Starting off
- django-admin startproject PROJECT_NAME
- python manage.py startapp APP_NAME
- add the APP in settings.py's INSTALLED_APPS
- create the view in views.py in the APP
- create urls.py in the APP
- configure the urls.py in the PROJECT

## Django
### Templates
- in urls.py add `app_name = 'APP_NAME'`
- `{% url 'APP_NAME:URL_NAME' %}` changes to the url named `URL_NAME` in the app called `APP_NAME`
- csrf middleware is added by default
- add `{% csrf_token %}` in the html form to make it valid
- Lecture 1: 1:20:00 Django forms
- `HttpResponseRedirect(reverse('APP_NAME:URL_NAME'))`
- request.session
- next attribute can be used to store the previous page's directory and get back to it later
- next_ = request.GET.get('next', reverse('index'))
### Custom Filters/Tags
- we can register tags in 'app/templatetags' dir
- they can then be registered in 'settings/TEMPLATES/OPTIONS/builtins' in order to work without having to load them using the {%load%} tag
	- https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/
	- https://docs.djangoproject.com/en/3.1/topics/templates/#django.template.backends.django.DjangoTemplates

## React
- We need to import React, ReactDOM and Babel
```JavaScript
class APP_NAME extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			stateItem1Key: stateItem1Val,
			stateItem2Key: stateItem2Val
		}
	}

	render() {
		return (
			<div>
				this.state.stateItem1Key
			</div>
		)
	}
}

ReactDOM.render(<APP_NAME/>, parentNode)
```
