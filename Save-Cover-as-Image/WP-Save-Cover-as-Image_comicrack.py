#@Name  WP - Save Cover as Image
#@Key   SaveCoverAsImage             [Defaults to function name]
#@Hook  Books
import clr

from System import *
from System.IO import FileInfo, Path

clr.AddReference("System.Drawing")
from System.Drawing import *
from System.Drawing.Imaging import *

def SaveCoverAsImage(books):
	for book in books:
		bookFileInfo = FileInfo(book.FilePath)
		bookNameWithoutExt = Path.GetFileNameWithoutExtension(book.FilePath);
		dirName = bookFileInfo.DirectoryName
		
		destinationFilePath = dirName + "\\" + bookNameWithoutExt + '.jpg'
		
		pageImage = ComicRack.App.GetComicPage(book, book.FrontCoverPageIndex)
		pageImage.Save(destinationFilePath, ImageFormat.Jpeg)
