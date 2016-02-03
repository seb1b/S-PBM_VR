# -*- coding: utf-8 -*-
import PASS

def buildHelper(manager, model):
	# SID
	baseLayer = model.hasModelComponent[0]
	baseLayer.setMetaContent("Date", "01.01.2016")
	
	# SID -> Subjects
	sKonstrukteur = baseLayer.addSubject()
	sKonstrukteur.label.append("Konstrukteur")
	sKonstrukteur.hasAbstractVisualRepresentation.setPoint2D(-0.4, -0.2)
	sKonstrukteur.setMetaContent("Date", "01.01.2016")
	sPruefer = baseLayer.addSubject()
	sPruefer.label.append("Prüfer")
	sPruefer.setMetaContent("Date", "01.01.2016")
	sPruefer.hasAbstractVisualRepresentation.setPoint2D(-0.1, -0.2)
	sEntwicklungsleiter = baseLayer.addSubject()
	sEntwicklungsleiter.label.append("Entwicklungsleiter")
	sEntwicklungsleiter.setMetaContent("Date", "01.01.2016")
	sEntwicklungsleiter.hasAbstractVisualRepresentation.setPoint2D(-0.1, 0.2)
	sPrototypenbau = baseLayer.addSubject()
	sPrototypenbau.label.append("Prototypenbau")
	sPrototypenbau.setMetaContent("Date", "01.01.2016")
	sPrototypenbau.hasAbstractVisualRepresentation.setPoint2D(0.2, -0.2)
	sSerienfertigung = baseLayer.addSubject()
	sSerienfertigung.label.append("Serienfertigung")
	sSerienfertigung.setMetaContent("Date", "01.01.2016")
	sSerienfertigung.hasAbstractVisualRepresentation.setPoint2D(0.4, -0.2)
	# SID -> MessageExchanges
	meKonstrukteurPruefer = baseLayer.addMessageExchange(sKonstrukteur, sPruefer)
	meKonstrukteurPruefer.label.append("Änderungsantrag")
	meKonstrukteurPruefer.setMetaContent("Date", "01.01.2016")
	meKonstrukteurPruefer.hasAbstractVisualRepresentation.setPoint2D(-0.3, -0.17)
	mePrueferKonstrukteur = baseLayer.addMessageExchange(sPruefer, sKonstrukteur)
	mePrueferKonstrukteur.label.append("Antrag überarbeiten")
	mePrueferKonstrukteur.setMetaContent("Date", "01.01.2016")
	mePrueferKonstrukteur.hasAbstractVisualRepresentation.setPoint2D(-0.3, -0.23)
	mePrueferEntwicklungsleiter = baseLayer.addMessageExchange(sPruefer, sEntwicklungsleiter)
	mePrueferEntwicklungsleiter.label.append("Änderungsantrag in Ordnung")
	mePrueferEntwicklungsleiter.setMetaContent("Date", "01.01.2016")
	mePrueferEntwicklungsleiter.hasAbstractVisualRepresentation.setPoint2D(-0.1, 0)
	meEntwicklungsleiterPrototypenbau = baseLayer.addMessageExchange(sEntwicklungsleiter, sPrototypenbau)
	meEntwicklungsleiterPrototypenbau.label.append("Freigabe Prototypenbau")
	meEntwicklungsleiterPrototypenbau.setMetaContent("Date", "01.01.2016")
	meEntwicklungsleiterPrototypenbau.hasAbstractVisualRepresentation.setPoint2D(-0.05, 0)
	meEntwicklungsleiterSerienfertigung = baseLayer.addMessageExchange(sEntwicklungsleiter, sSerienfertigung)
	meEntwicklungsleiterSerienfertigung.label.append("Freigabe der Serienfertigung")
	meEntwicklungsleiterSerienfertigung.setMetaContent("Date", "01.01.2016")
	meEntwicklungsleiterSerienfertigung.hasAbstractVisualRepresentation.setPoint2D(0.4, 0)
	mePrototypenbauEntwicklungsleiter = baseLayer.addMessageExchange(sPrototypenbau, sEntwicklungsleiter)
	mePrototypenbauEntwicklungsleiter.label.append("Prototyp funktional")
	mePrototypenbauEntwicklungsleiter.setMetaContent("Date", "01.01.2016")
	mePrototypenbauEntwicklungsleiter.hasAbstractVisualRepresentation.setPoint2D(0.05, 0)
	mePrototypenbauKonstrukteur = baseLayer.addMessageExchange(sPrototypenbau, sKonstrukteur)
	mePrototypenbauKonstrukteur.label.append("Prototyp nicht funktional")
	mePrototypenbauKonstrukteur.setMetaContent("Date", "01.01.2016")
	mePrototypenbauKonstrukteur.hasAbstractVisualRepresentation.setPoint2D(0, -0.25)
	
	# SBD (Konstrukteur)
	behaviorKonstrukteur = sKonstrukteur.hasBehavior
	# SBD -> States
	state1 = behaviorKonstrukteur.addReceiveState()
	state1.label.append("Warten auf Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(-0.2,0.1)
	behaviorKonstrukteur.setInitialState(state1)
	state2 = behaviorKonstrukteur.addFunctionState()
	state2.label.append("Prüfe Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.1)
	state3 = behaviorKonstrukteur.addSendState()
	state3.label.append("Bitte um Freigabe")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.2,0.1)
	state4 = behaviorKonstrukteur.addReceiveState()
	state4.label.append("Ende")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.4,0.1)
	state4.isFinalState = True
	state5 = behaviorKonstrukteur.addSendState()
	state5.label.append("Informiere Konstrukteur")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.3)
	
	# SBD -> TransitionEdges
	edge12 = behaviorKonstrukteur.addReceiveTransition(state1, state2, mePrueferKonstrukteur)
	edge12.label.append("Änderungsantrag")
	edge12.hasAbstractVisualRepresentation.setPoint2D(0.1,0.1)
	edge23 = behaviorKonstrukteur.addStandardTransition(state2, state3)
	edge23.label.append("Antrag OK")
	edge23.hasAbstractVisualRepresentation.setPoint2D(0.2,0.1)
	edge25 = behaviorKonstrukteur.addStandardTransition(state2, state5)
	edge25.label.append("Antrag nicht OK")
	edge25.hasAbstractVisualRepresentation.setPoint2D(0.3,0.1)
	edge34 = behaviorKonstrukteur.addSendTransition(state3, state4, meKonstrukteurPruefer)
	edge34.label.append("Änderungsantrag in Ordnung")
	edge34.hasAbstractVisualRepresentation.setPoint2D(0.4,0.1)
	edge42 = behaviorKonstrukteur.addReceiveTransition(state4, state2, mePrueferKonstrukteur)
	edge42.label.append("Änderungsantrag")
	edge42.hasAbstractVisualRepresentation.setPoint2D(0.5,0.1)

	# SBD (Pruefer)
	behaviorPruefer = sPruefer.hasBehavior
	# SBD -> States
	state1 = behaviorPruefer.addReceiveState()
	state1.label.append("Warten auf Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(-0.2,0.1)
	behaviorPruefer.setInitialState(state1)
	state2 = behaviorPruefer.addFunctionState()
	state2.label.append("Prüfe Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.1)
	state3 = behaviorPruefer.addSendState()
	state3.label.append("Bitte um Freigabe")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.2,0.1)
	state4 = behaviorPruefer.addReceiveState()
	state4.label.append("Ende")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.4,0.1)
	state4.isFinalState = True
	state5 = behaviorPruefer.addSendState()
	state5.label.append("Informiere Konstrukteur")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.3)
	
	# SBD -> TransitionEdges
	edge12 = behaviorPruefer.addReceiveTransition(state1, state2, meKonstrukteurPruefer)
	edge12.label.append("Änderungsantrag")
	edge23 = behaviorPruefer.addStandardTransition(state2, state3)
	edge23.label.append("Antrag OK")
	edge25 = behaviorPruefer.addStandardTransition(state2, state5)
	edge25.label.append("Antrag nicht OK")
	edge34 = behaviorPruefer.addSendTransition(state3, state4, mePrueferEntwicklungsleiter)
	edge34.label.append("Änderungsantrag in Ordnung")
	edge42 = behaviorPruefer.addReceiveTransition(state4, state2, meKonstrukteurPruefer)
	edge42.label.append("Änderungsantrag")

	# SBD (Entwicklungsleiter)
	behaviorEntwicklungsleiter = sEntwicklungsleiter.hasBehavior
	# SBD -> States
	state1 = behaviorEntwicklungsleiter.addReceiveState()
	state1.label.append("Warten auf Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(-0.2,0.1)
	behaviorEntwicklungsleiter.setInitialState(state1)
	state2 = behaviorEntwicklungsleiter.addFunctionState()
	state2.label.append("Prüfe Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.1)
	state3 = behaviorEntwicklungsleiter.addSendState()
	state3.label.append("Bitte um Freigabe")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.3,0.1)
	state4 = behaviorEntwicklungsleiter.addReceiveState()
	state4.label.append("Ende")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.4,0.1)
	state4.isFinalState = True
	state5 = behaviorEntwicklungsleiter.addSendState()
	state5.label.append("Informiere Konstrukteur")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.3)
	
	# SBD -> TransitionEdges
	edge12 = behaviorEntwicklungsleiter.addReceiveTransition(state1, state2, mePrueferEntwicklungsleiter)
	edge12.label.append("Änderungsantrag")
	edge23 = behaviorEntwicklungsleiter.addStandardTransition(state2, state3)
	edge23.label.append("Antrag OK")
	edge25 = behaviorEntwicklungsleiter.addStandardTransition(state2, state5)
	edge25.label.append("Antrag nicht OK")
	edge34 = behaviorEntwicklungsleiter.addSendTransition(state3, state4, meEntwicklungsleiterPrototypenbau)
	edge34.label.append("Änderungsantrag in Ordnung")
	edge42 = behaviorEntwicklungsleiter.addReceiveTransition(state4, state2, mePrueferEntwicklungsleiter)
	edge42.label.append("Änderungsantrag")

	# SBD (Prototypenbau)
	behaviorPrototypenbau = sPrototypenbau.hasBehavior
	# SBD -> States
	state1 = behaviorPrototypenbau.addReceiveState()
	state1.label.append("Warten auf Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(-0.2,0.1)
	behaviorPrototypenbau.setInitialState(state1)
	state2 = behaviorPrototypenbau.addFunctionState()
	state2.label.append("Prüfe Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.1)
	state3 = behaviorPrototypenbau.addSendState()
	state3.label.append("Bitte um Freigabe")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.2,0.1)
	state4 = behaviorPrototypenbau.addReceiveState()
	state4.label.append("Ende")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.4,0.1)
	state4.isFinalState = True
	state5 = behaviorPrototypenbau.addSendState()
	state5.label.append("Informiere Konstrukteur")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.3)
	
	# SBD -> TransitionEdges
	edge12 = behaviorPrototypenbau.addReceiveTransition(state1, state2, meEntwicklungsleiterPrototypenbau)
	edge12.label.append("Änderungsantrag")
	edge23 = behaviorPrototypenbau.addStandardTransition(state2, state3)
	edge23.label.append("Antrag OK")
	edge25 = behaviorPrototypenbau.addStandardTransition(state2, state5)
	edge25.label.append("Antrag nicht OK")
	edge34 = behaviorPrototypenbau.addSendTransition(state3, state4, mePrototypenbauKonstrukteur)
	edge34.label.append("Änderungsantrag in Ordnung")
	edge42 = behaviorPrototypenbau.addReceiveTransition(state4, state2, meEntwicklungsleiterPrototypenbau)
	edge42.label.append("Änderungsantrag")

	# SBD (Serienfertigung)
	behaviorSerienfertigung = sSerienfertigung.hasBehavior
	# SBD -> States
	state1 = behaviorSerienfertigung.addReceiveState()
	state1.label.append("Warten auf Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(-0.2,0.1)
	behaviorSerienfertigung.setInitialState(state1)
	state2 = behaviorSerienfertigung.addFunctionState()
	state2.label.append("Prüfe Antrag")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.1)
	state3 = behaviorSerienfertigung.addSendState()
	state3.label.append("Bitte um Freigabe")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.2,0.1)
	state4 = behaviorSerienfertigung.addReceiveState()
	state4.label.append("Ende")
	state1.hasAbstractVisualRepresentation.setPoint2D(0.4,0.1)
	state4.isFinalState = True
	state5 = behaviorSerienfertigung.addSendState()
	state5.label.append("Informiere Konstrukteur")
	state1.hasAbstractVisualRepresentation.setPoint2D(0,0.3)
	
	# SBD -> TransitionEdges
	edge23 = behaviorSerienfertigung.addStandardTransition(state2, state3)
	edge23.label.append("Antrag OK")
	edge25 = behaviorSerienfertigung.addStandardTransition(state2, state5)
	edge25.label.append("Antrag nicht OK")

#Create manager
manager = PASS.ModelManager()
#Now build the model
buildHelper(manager, manager.model)

#Save
manager.saveAs("./tests/Beispielprozess.owl")
#Load
manager2 = PASS.ModelManager("./tests/Beispielprozess.owl")
manager2.saveAs("./tests/Beispielprozess_copy.owl")
