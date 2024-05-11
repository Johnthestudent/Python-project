# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
from bs4 import BeautifulSoup

class UnhandledException(Exception):
	pass


def rss_parser(
	xml: str,
	limit: Optional[int] = None,
	json: bool = False,
) -> List[str]:
	"""
	RSS parser.

	Args:
		xml: XML document as a string.
		limit: Number of the news to return. if None, returns all news.
		json: If True, format output as JSON.

	Returns:
		List of strings.
		Which then can be printed to stdout or written to file as a separate lines.

	Examples:
		>>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
		>>> rss_parser(xml)
		["Feed: Some RSS Channel",
		"Link: https://some.rss.com"]
		>>> print("\\n".join(rss_parser(xmls)))
		Feed: Some RSS Channel
		Link: https://some.rss.com
	"""
	# Code reads xml data from the rss url 
	xml = requests.get('https://news.yahoo.com/rss')
	soup = BeautifulSoup(xml.content, 'xml')
	entries = soup.find_all('entry')
	
	for entry in entries:
		channel = entry.channel
		title = entry.channel.title.text
		link = entry.channel.link['href']
		lastBuildDate = entry.channel.lastBuildDate
		pubDate = entry.channel.pubDate
		for category in categories:
			category = entry.channel.category
		managinEditor = entry.channel.managinEditor
		description = entry.channel.description
		for item in items:
			item = entry.item
			title = entry.item.title
			author = entry.item.author
			pubDate = entry.item.pubDate
			link = entry.item.link['href']
			category = entry.item.category
			description = entry.item.description
	
	result_of_it = f"Channel: Title: {title}\n Link: {link}\n LastBuildDate : {lastBuildDate}\n PubDate: {pubDate}\n Categories: \n \t Category: {category}\n MagainEditor: {managinEditor}\n Description: {description}\n Items:\n \t Item: {item}\n \t\t Title: {title}\n \t\t Author: {author}\n \t\t PubDate: {pubDate}\n \t\t Link: {link}\n \t\t Category: {category}\n \t\t Description: {description}"
	print(result_of_it)
	return(result_of_it)

def main(argv: Optional[Sequence] = None):
	"""
	The main function of your task.
	"""
	parser = ArgumentParser(
		prog="rss_reader",
		description="Pure Python command-line RSS reader.",
	)
	parser.add_argument("source", help="RSS URL", type=str, nargs="?")
	parser.add_argument(
		"--json", help="Print result as JSON in stdout", action="store_true"
	)
	parser.add_argument(
		"--limit", help="Limit news topics if this parameter provided", type=int
	)

	args = parser.parse_args(argv)
	xml = requests.get(args.source).text
	try:
		print("\n".join(rss_parser(xml, args.limit, args.json)))
		return 0
	except Exception as e:
		raise UnhandledException(e)


if __name__ == "__main__":
	main()
