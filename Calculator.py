import csv
from os import pread
import time
from anytree import Node, RenderTree
from anytree.iterators.postorderiter import PostOrderIter
from anytree.render import ContRoundStyle
from itertools import groupby
from operator import itemgetter

printOutput = True
printTrees = True

start = time.time()
fileName = "Victor/mainFile.csv"
with open(fileName, "r") as currentFile:
    dataList = list(csv.reader(currentFile, delimiter=","))[1:]

newFile = "Victor/calculatedResults.csv"
with open(newFile, "w", encoding="utf-8", newline="") as nextFile:
    writer = csv.writer(nextFile, delimiter=",")
    header = ["Material", "Primary Requirement", "Level", "Child Component", "Secondary Requirement"]
    writer.writerow(header)

    for uniqueMaterial, materialGroup in groupby(dataList, itemgetter(0)):

        listOfNodes = []
        listOfNodes.append(Node(uniqueMaterial, material=uniqueMaterial))

        for material, pRequirement, pComponent, level, cComponent, ccAmount in materialGroup:
            
            listOfNodes[0].ccAmount = float(pRequirement)
            listOfNodes.append(
                Node(
                    cComponent,
                    parentID=pComponent,
                    ccAmount=float(ccAmount),
                    material=uniqueMaterial,
                    pRequirement=pRequirement,
                    level=level,
                )
            )

        for aNode in listOfNodes:
            for bNode in listOfNodes[1:]:
                if bNode.parentID == aNode.name:
                    bNode.parent = aNode

        for aNode in PostOrderIter(listOfNodes[0]):
            for bNode in PostOrderIter(aNode):
                if bNode == aNode:
                    continue
                else:
                    bNode.ccAmount = round(bNode.ccAmount * aNode.ccAmount, 3)

        if printTrees:
            print()
            print(RenderTree(listOfNodes[0], style=ContRoundStyle).by_attr())

        if printOutput:
            print("\nPrimary Requirement:")
            print(listOfNodes[0].name, "---", listOfNodes[0].ccAmount)

            print("\nSecondary Requirement:")
            for eachNode in listOfNodes[1:]:
                print(eachNode.name, "---", eachNode.ccAmount)
            print("-------------------")

        for eachNode in listOfNodes[1:]:
            output = [
                eachNode.material,
                eachNode.pRequirement,
                eachNode.level,
                eachNode.name,
                eachNode.ccAmount,
            ]
            writer.writerow(output)

end = time.time()
print("Calculated in", round(end - start, 3), "seconds")