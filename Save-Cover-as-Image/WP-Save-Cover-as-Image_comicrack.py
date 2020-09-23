#@Name  Save Cover as Image...
#@Key   SaveCoverAsImage             [Defaults to function name]
#@Hook  Books
import clr
from System import *
from System.IO import *
clr.AddReference("System.Drawing")
from System.Drawing import *
from System.Drawing.Imaging import *
clr.AddReferenceByPartialName("System.Windows.Forms")
from System.Windows.Forms import Clipboard, FolderBrowserDialog, DialogResult, MessageBox

def SaveCoverAsImage(books):
	folderDialog = FolderBrowserDialog()
	folderDialog.Description = 'Select the destination to which selected eComics will be moved. \nExisting files in the destination folder will NOT be overwritten.'
	folderDialog.ShowNewFolderButton = True
	if folderDialog.ShowDialog(ComicRack.MainWindow) == DialogResult.OK:
		destinationFolder = folderDialog.SelectedPath + "\\"
		
		if Directory.Exists(destinationFolder):
			for book in books:
				pageNameString = "Cover"
				destinationFilePath = destinationFolder + CreateComicName(book) + ' Page' + pageNameString + '.jpg'
				
				pageImage = ComicRack.App.GetComicPage(book, book.FrontCoverPageIndex)
				pageImage.Save(destinationFilePath, ImageFormat.Jpeg)
			
def CreateComicName(book):

	series = book.ShadowSeries
	series = series.replace('?', '')
	series = series.replace('/', '')
	series = series.replace('\\', '')
	series = series.replace('*', '')
	series = series.replace(':', ' -')
	series = series.replace('<', '[')
	series = series.replace('>', ']')
	series = series.replace('|', '!')
	volume = ""
	numeral = ""
	count = ""
	year = ""
	if series != "":
		if book.ShadowVolume != -1:
			volume = " V" + str(book.ShadowVolume)
			
		if book.ShadowNumber != "":
			try:
				numeral = "%.3d" % int(book.ShadowNumber)
				if (book.ShadowCount > 0) and (book.ShadowCount >= int(numeral)):
					count = " (of " + "%.3d" % book.ShadowCount + ")"
			except ValueError:
				numeral = book.ShadowNumber
				numeral = numeral.replace('?', '')
				numeral = numeral.replace('/', ' ')
				numeral = numeral.replace('\\', ' ')
				numeral = numeral.replace('*', ' ')
				numeral = numeral.replace(':', '-')
				numeral = numeral.replace('<', '[')
				numeral = numeral.replace('>', ']')
				numeral = numeral.replace('|', '!')
				numeral = numeral.replace('"', '\'').strip()
			if len(numeral) > 0:
				numeral = " " + numeral
				
		if book.ShadowYear > 1900:
			year = " (" + str(book.ShadowYear) + ")"
			
		return series + volume + numeral + count + year